""" Contents Schema
    Request/Response format
"""

from sqlalchemy import Column, Integer, String, DateTime
from db.config import Base


class ContentsModel(Base):
    """The final Item Model

    This is our final source of truth.

    """

    __tablename__ = "contents"
    id = Column(Integer, primary_key=True)
    item_slot = Column(Integer)
    item_count = Column(Integer)
    item_id = Column(String)

    class Conifg:
        orm_mode = True
