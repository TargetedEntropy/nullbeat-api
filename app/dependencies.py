"""Dependencies to load DALs
"""
from db.config import db_session
from db.dals.item_dal import ItemDAL
from db.dals.job_dal import JobDAL


async def get_item_dal():
    """Access the basic db account functions

    This is the Item DAL used to acess the
    database.

    Parameters
    ----------
    None

    """
    yield ItemDAL(db_session)




async def get_job_dal():
    """Access the basic db account functions

    This is the Job DAL used to acess the
    database.

    Parameters
    ----------
    None

    """
    yield JobDAL(db_session)
