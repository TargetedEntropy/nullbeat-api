from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class JobModel(BaseModel):
    id: Optional[int]
    job_type: Optional[str]
    character_name: Optional[str]
    job_completed: Optional[bool]
    nbt_data: Optional[str]

    class Config:
        orm_mode = True
