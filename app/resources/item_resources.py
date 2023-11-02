from fastapi import Depends
from dependencies import get_item_dal


class ItemClass:
    """A class to interact with the items

    This is where we use the Item DAL to respond to the
    routers. Creating, getting items and thier paramters
    is done from this class.

    Attributes
    ----------
    ItemDAL : the item data access layer

    """

    def __init__(self, ItemDAL=Depends(get_item_dal)):
        """
        Parameters
        ----------
        ItemDAL : class
        
        The item data access layer
        """
        self.ItemDAL = ItemDAL

    async def get_item(self, item_data):
        """Get an item

        Return any and all infomration we have
        about an item.

        """
        return await self.ItemDAL.get_item(item_data)

    async def set_item(self, item_data: str):
        """Add an Item
        """
        return await self.ItemDAL.set_item(item_data)
