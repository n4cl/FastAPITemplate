from fastapi import FastAPI, Body
from logging_template.logging.logger import get_logger

app = FastAPI()
logger = get_logger(__name__)


@app.post("/")
async def post(body=Body(...)):
    logger.info(body)
    return  {"message": "Input data has been accepted"}


@app.get("/hello")
async def hello():
    return {"message": "hello world!"}
