from fastapi import FastAPI, Form, Request

app = FastAPI()

@app.get("/")
def index(request: Request):
    return {"Hello world"}
