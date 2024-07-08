from enum import Enum

from fastapi import FastAPI  # type: ignore

app = FastAPI()


@app.get("/")
async def root():
    return {"Hello": "World"}


@app.post("/")
async def post():
    return {"message": "Hello from post request"}


@app.put("/")
async def put():
    return {"message": "Hello from put request"}


@app.get("/users")
async def users():
    return {"message": "List of users"}


@app.get("/users/me")
async def current_user():
    return {"Message": "the current user is you"}


@app.get("/users/{user_id}")
async def get_user(user_id: str):
    return {"user_id": f"Hello, {user_id}"}


class FoodEnum(str, Enum):
    fruits = "fruits"
    vegetables = "vegetables"
    dairy = "dairy"


@app.get("/foods/{food_name}")
async def get_food(food_name: FoodEnum):
    if food_name == FoodEnum.vegetables:
        return {"food_name": food_name, "message": "This is a vegetable"}

    if food_name == "fruits":
        return {"food_name": food_name, "message": "This is a fruit"}

    return {"food_name": food_name, "message": "This is a dairy product"}
