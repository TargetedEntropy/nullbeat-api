"""Dependencies to load DALs
"""
from db.config import db_session
from db.dals.item_dal import ItemDAL
from db.dals.job_dal import JobDAL
from db.dals.character_dal import CharacterDAL


async def get_item_dal():
    """Access the basic db item functions

    This is the Item DAL used to acess the
    database.

    Parameters
    ----------
    None

    """
    yield ItemDAL(db_session)




async def get_job_dal():
    """Access the basic db job functions

    This is the Job DAL used to acess the
    database.

    Parameters
    ----------
    None

    """
    yield JobDAL(db_session)




async def get_character_dal():
    """Access the basic db character functions

    This is the Character DAL used to acess the
    database.

    Parameters
    ----------
    None

    """
    yield CharacterDAL(db_session)
