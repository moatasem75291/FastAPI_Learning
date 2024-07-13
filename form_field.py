from pydantic import BaseModel

from fastapi import FastAPI, Form

app = FastAPI()


@app.post("/login-form")
async def login_form(user_name: str = Form(...), password: str = Form(...)):
    return {"user name": user_name}


class User(BaseModel):
    user_name: str
    password: str


@app.post("/login-json")
async def login_json(user: User):
    return user
