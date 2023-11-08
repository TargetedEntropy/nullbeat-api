"""Jobs Router
"""

from urllib import parse
from fastapi import APIRouter, Depends, Request
from resources.job_resources import JobClass
from db.models.job_model import JobModel


job_router = APIRouter()

@job_router.get("/job")
async def get_job(request: Request, job_depends=Depends(JobClass)):
    """Get an job based on filters."""
    try:
        job_data = parse.parse_qs(parse.urlsplit(str(request.url)).query)
        return await job_depends.get_job(job_data)
    except Exception as error:
        return error


@job_router.post("/job")
async def set_job(job: JobModel, job_depends=Depends(JobClass)):
    """Add an job"""
    # job_data = await request.json()
    return await job_depends.set_job(job)
