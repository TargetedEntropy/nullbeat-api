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
    displayName = Column(String)
    itemGroups = Column(String)
    count = Column(Integer)
    maxCount = Column(Integer)
    name = Column(String)
    tags = Column(String)
    nbt = Column(String, nullable=True)

    class Conifg:
        orm_mode = True

