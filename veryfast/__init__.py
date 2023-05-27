import logging

from fastapi import FastAPI

app = FastAPI()

logger = logging.getLogger(__name__)


@app.get("/")
async def root_endpoint():
    logger.info("root")
    return {"message": "Hello World"}


@app.get("/version")
async def get_version():
    logger.info("getting the app version")
    logger.debug("This is debug level info")
    return {"version": "1.0.2"}
