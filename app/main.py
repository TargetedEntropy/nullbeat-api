from fastapi import FastAPI
from routers.item_router import item_router
from routers.job_router import job_router
from routers.character_router import character_router

import logging

logging.basicConfig(
    level=logging.DEBUG, format="%(levelname)s:\t%(asctime)s:%(message)s"
)

description = """The Storage backend for the nullbeat logistics system"""

app = FastAPI(title="nullbeat-api", description=description, version="0.2.0")

logging.debug("Loading routers")
app.include_router(item_router)
app.include_router(job_router)
app.include_router(character_router)

