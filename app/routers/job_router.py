"""Jobs Router
"""

from urllib import parse
from fastapi import APIRouter, Depends, Request
from resources.job_resources import JobClass


job_router = APIRouter()


@job_router.get("/job")
async def get_job(request: Request, job_depends=Depends(JobClass)):
    """Get a job"""
    try:
        data = parse.parse_qs(parse.urlsplit(str(request.url)).query)
        return await job_depends.get_job(data)
    except Exception as error:
        return error


@job_router.post("/job")
async def set_job(request: Request, job_depends=Depends(JobClass)):
    """Update a job"""
    data = await request.json()
    return await job_depends.set_job(data)
    
