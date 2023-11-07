""" Item Schema
    Request/Response format
"""

from sqlalchemy import Column, Integer, String, DateTime
from db.config import Base


class ItemModel(Base):
    """The final Item Model

    This is our final source of truth.

    """

    __tablename__ = "item"
    id = Column(Integer, primary_key=True)
    item_name = Column(String)
    item_contents = Column(String)
    character_name = Column(String)
    nbt_data = Column(String)

    class Conifg:
        orm_mode = True
