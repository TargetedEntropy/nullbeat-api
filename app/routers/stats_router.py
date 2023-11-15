"""Items Router
"""

from fastapi import APIRouter, Depends
from resources.item_resources import ItemClass


stats_router = APIRouter()


@stats_router.get("/stats")
async def get_stats(stats_depends=Depends(ItemClass)):
    """Get overall stats"""
    try:
        return await stats_depends.get_stats()
    except Exception as error:
        return error

