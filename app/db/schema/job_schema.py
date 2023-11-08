""" Job Schema
    Request/Response format
"""

from sqlalchemy import Column, Integer, String, Boolean
from db.config import Base


class JobSchema(Base):
    """The Job Model

    This is our final source of truth.

    """

    __tablename__ = "job"
    id = Column(Integer, primary_key=True)
    job_type = Column(String)
    character_name = Column(String)
    job_completed = Column(Boolean)
    nbt_data = Column(String)

    # nbt_data = Column(String)

    class Conifg:
        orm_mode = True
