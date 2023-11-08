from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class CharacterModel(BaseModel):
    # id: Optional[int]
    character_name: Optional[str]
    character_pass: Optional[str]
    account_type: Optional[str]

    class Config:
        orm_mode = True
