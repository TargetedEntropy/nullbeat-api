""" JobDAL

    Job DataLayer, access to the database directly from routed functions.
"""
import json
from datetime import datetime
from db.config import db_session
from db.schema.job_schema import JobSchema
from db.tables.job_table import JobTable
import sqlalchemy as sa


class JobDAL:
    """A class to interact with the job model in the DB

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

    async def get_job(self):
        """Get info for a job

        This is where we finally ask the database
        itself about our job..

        Returns:
            str: json about our job
        """

        query = self.db_session.query(JobSchema)
        # for attr, value in data.jobs():
        query = query.filter(JobSchema.job_completed == False)

        results = query.all()
        return results

    async def set_job(self, data: str):
        """Update a

        Args:
            job_data (str): Information we have about an job

        Returns:
            str: Repeat the information we were provided
        """
        print(f"Inserting Values: {data}")
        job = JobSchema(
            job_type=data.job_type,
            job_completed=data.job_completed,
            character_name=data.character_name,
            nbt_data=json.dumps(data.nbt_data),
        )
        print(f"data: {job}")

        print(self.db_session.add(job))
        print(self.db_session.commit())

        return "Success"
