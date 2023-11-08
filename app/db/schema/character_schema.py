""" Character Schema
    Request/Response format
"""

from sqlalchemy import Column, Integer, String, Boolean
from db.config import Base


class CharacterSchema(Base):
    """The Character Model

    This is our final source of truth.

    """

    __tablename__ = "character"
    id = Column(Integer, primary_key=True)
    character_name = Column(String)
    character_pass = Column(String)
    account_type = Column(String)

    class Conifg:
        orm_mode = True
