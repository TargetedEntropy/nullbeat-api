"""Characters Router
"""

from urllib import parse
from fastapi import APIRouter, Depends, Request
from resources.character_resources import CharacterClass
from db.models.character_model import CharacterModel


character_router = APIRouter()

@character_router.get("/character")
async def get_character(character_depends=Depends(CharacterClass)):
    """Get an character based on filters."""
    try:
        return await character_depends.get_character()
    except Exception as error:
        return error


@character_router.post("/character")
async def set_character(character: CharacterModel, character_depends=Depends(CharacterClass)):
    """Add an character"""
    # character_data = await request.json()
    return await character_depends.set_character(character)
