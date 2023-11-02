"""Items Router
"""

from urllib import parse
from fastapi import APIRouter, Depends, Request
from fastapi.responses import RedirectResponse
from resources.item_resources import ItemClass


item_router = APIRouter()


@item_router.get("/")
async def index():
    """Return the user to the docs page on index

    There's nothing on the frontpage so we send users
    to the documentation by default.

    """
    return RedirectResponse("/docs")

@item_router.get("/item")
async def get_item(request: Request, item_depends=Depends(ItemClass)):
    """Get an item based on filters.
    """
    try:
        item_data = parse.parse_qs(parse.urlsplit(str(request.url)).query)
        return await item_depends.get_item(item_data)
    except Exception as error:
        return error


@item_router.post("/item")
async def set_item(request: Request, item_depends=Depends(ItemClass)):
    """Add an item
    """
    item_data = await request.json()
    return await item_depends.set_item(item_data)

