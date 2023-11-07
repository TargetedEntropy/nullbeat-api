from fastapi import FastAPI
import routers.item_router as item_router
import routers.job_router as job_router

import logging

logging.basicConfig(
    level=logging.DEBUG, format="%(levelname)s:\t%(asctime)s:%(message)s"
)

description = """The Storage backend for the nullbeat logistics system"""

app = FastAPI(title="nullbeat-api", description=description, version="0.2.0")

logging.debug("Loading routers")
app.include_router(item_router.item_router)
app.include_router(job_router.job_router)

