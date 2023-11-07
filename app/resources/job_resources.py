from fastapi import Depends
from dependencies import get_job_dal


class JobClass:
    """A class to interact with the jobs

    This is where we use the Job DAL to respond to the
    routers. Creating, getting jobs and thier paramters
    is done from this class.

    Attributes
    ----------
    JobDAL : the job data access layer

    """

    def __init__(self, JobDAL=Depends(get_job_dal)):
        """
        Parameters
        ----------
        JobDAL : class

        The job data access layer
        """
        self.JobDAL = JobDAL

    async def get_job(self, data):
        """Get a job

        Return any and all infomration we have
        about a job.

        """
        return await self.JobDAL.get_job(data)

    async def set_job(self, data: str):
        """Update a Job"""
        return await self.JobDAL.set_job(data)
