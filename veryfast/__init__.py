import logging

from fastapi import FastAPI

app = FastAPI()

logger = logging.getLogger(__name__)

@app.get("/")
async def root():
    logger.info("root")
    return {"message": "Hello World"}
