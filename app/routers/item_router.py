"""Items Router
"""

from urllib import parse
from fastapi import APIRouter, Depends, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from resources.item_resources import ItemClass
import re
import luadata

item_router = APIRouter()

def parse_lua_table(lua_bytes):
    # Convert bytes to string
    lua_str = lua_bytes.decode('utf-8')
    
    # Remove newlines and leading/trailing whitespace
    lua_str = lua_str.strip().replace('\n', '')
    
    # Find key-value pairs using regular expressions
    pattern = r'\{(.*?)\}'
    matches = re.findall(pattern, lua_str)
    
    lua_table = []
    for match in matches:
        # Split each key-value pair into key and value
        pairs = match.split(',')
        item = {}
        for pair in pairs:
            # Check if the pair contains '='
            if '=' in pair:
                # Split key and value
                key_value = pair.split('=', 1)
                key = key_value[0].strip()
                value = '='.join(key_value[1:]).strip().strip('"')
                # Handle special case for 'itemGroups'
                if key == 'itemGroups':
                    # Extract nested braces content and split by comma
                    group_items = re.findall(r'\{(.*?)\}', value)
                    group_dict = {}
                    for group_item in group_items:
                        group_pairs = group_item.split(',')
                        for group_pair in group_pairs:
                            if '=' in group_pair:
                                group_key, group_value = group_pair.split('=', 1)
                                group_dict[group_key.strip()] = group_value.strip().strip('"')
                    item[key] = group_dict
                else:
                    item[key] = value
        lua_table.append(item)
    
    return lua_table



@item_router.get("/")
async def index():
    """Return the user to the docs page on index

    There's nothing on the frontpage so we send users
    to the documentation by default.

    """
    return RedirectResponse("/docs")


@item_router.get("/item")
async def get_item(request: Request, item_depends=Depends(ItemClass)):
    """Get an item based on filters."""
    try:
        item_data = parse.parse_qs(parse.urlsplit(str(request.url)).query)
        return await item_depends.get_item(item_data)
    except Exception as error:
        return error


@item_router.post("/item")
async def set_item(request: Request, item_depends=Depends(ItemClass)):
    """Add an item"""
    text = await request.body()
    # print(text)
    try:
        
        text = text.decode('cp1252').replace("\n", "")
    except Exception as error:
        print(f"error: {error}")
    item_data = luadata.unserialize(text, encoding="utf-8", multival=True)

    return await item_depends.set_item(item_data[0])
