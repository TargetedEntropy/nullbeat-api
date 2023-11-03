""" ItemDAL

    Item DataLayer, access to the database directly from routed functions.
"""
import json
from datetime import datetime
from db.config import db_session
from db.schema.item_schema import ItemModel
from db.schema.contents_schema import ContentsModel
from db.tables.item_table import ItemTable
from db.tables.contents_table import ContentsTable
import sqlalchemy as sa


class ItemDAL:
    """A class to interact with the account model in the DB

    Attributes
    ----------
    database : the database object

    """

    def __init__(self, db_session: db_session):
        """
        Parameters
        ----------
        database : class
            The database object
        """
        self.db_session = db_session

    async def get_item(self, item_data):
        """Get info for an item

        This is where we finally ask the database
        itself about our item..

        Args:
            item_data (str): The item identifier

        Returns:
            str: json about our item
        """

        query = self.db_session.query(ItemModel)
        for attr, value in item_data.items():
            query = query.filter(getattr(ItemModel, attr) == value)

        results = query.all()
        return results

    async def set_item(self, item_data: str):
        """Save an Item

        Args:
            item_data (str): Information we have about an item

        Returns:
            str: Repeat the information we were provided
        """
        print(f"Inserting Values: {item_data['item_name']}")
        item = ItemModel(
            item_name=item_data["item_name"],
            item_contents=json.dumps(item_data["item_contents"]),
            character_name=item_data["character_name"],
        )

        print(f"Item: {item}")
        self.db_session.add(item)
        self.db_session.commit()
        return "Success"
