import logging

from fastapi import FastAPI

from veryfast.utils.compute import xvf_info

app = FastAPI()

logger = logging.getLogger(__name__)

logger.info(f"My name was set to '{__name__}'")


@app.get("/")
async def root_endpoint():
    logger.info("root")
    return {"message": "Hello World"}


@app.get("/version")
async def get_version():
    logger.info("getting the app version")
    logger.debug("This is debug level info")
    xvf_info()
    return {"version": "1.0.2"}
