""" ItemDAL

    Item DataLayer, access to the database directly from routed functions.
"""
import json
from db.config import db_session
from db.schema.item_schema import ItemModel
from db.schema.contents_schema import ContentsModel
from db.tables.item_table import ItemTable
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
        item = ItemModel(
            item_name=item_data["item_name"],
            item_contents=json.dumps(item_data["item_contents"]),
            character_name=item_data["character_name"],
            nbt_data=item_data["nbt_data"],
        )

        self.db_session.add(item)
        self.db_session.commit()
        self.db_session.flush()

        for item_content in item_data["item_contents"]:

            contents = ContentsModel(
                shulker_id=item.id,
                item_slot=item_content["Slot"],
                item_count=item_content["Count"],
                item_id=item_content["id"],
            )
            self.db_session.add(contents)
            self.db_session.commit()

        return "Success"


    def get_count(q):
        count_q = q.statement.with_only_columns([func.count()]).order_by(None)
        count = q.session.execute(count_q).scalar()
        return count


    async def get_stats(self):
        """Get info for an item

        This is where we finally ask the database
        itself about our item..

        Args:
            item_data (str): The item identifier

        Returns:
            str: json about our item
        """
        fun_time = {}
        fun_time['Characters Tracked'] = self.db_session.query(ItemModel).distinct(ItemModel.character_name).group_by(ItemModel.character_name).count()
        fun_time['Total Items'] = self.db_session.query(ContentsModel).count()
        fun_time['Container Count'] = self.db_session.query(ItemModel).count()

        return fun_time