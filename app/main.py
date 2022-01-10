from fastapi import FastAPI, Body

app = FastAPI()


@app.post("/")
async def post(body=Body(...)):
    print(body)
    return  {"message": "Input data has been accepted"}


@app.get("/hello")
async def hello():
    return {"message": "hello world!"}
