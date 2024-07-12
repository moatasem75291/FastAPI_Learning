from typing import Literal

from pydantic import BaseModel, EmailStr
from fastapi import FastAPI


app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float = 10.5
    tags: list[int] = []


items = {
    "foo": {
        "name": "Foo",
        "description": "A very nice Item",
        "price": 50.2,
        "tax": 10.5,
    },
    "bar": {
        "name": "Bar",
        "description": "Another Item for you",
        "price": 62,
        "tax": 10.5,
    },
}


@app.post("/items/")
async def create_item(item: Item):
    return item


@app.get("/items/{item_id}", response_model=Item, response_model_exclude_unset=True)
async def read_item(item_id: Literal["foo", "bar"]):
    return items[item_id]


class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: str


class UserIn(UserBase):
    password: str


class UserOut(UserBase):
    pass


@app.post("/users/", response_model=UserOut)
async def create_user(user: UserIn):
    return user


@app.get("/items/{item_id}/name", response_model=Item)
async def read_item_name(item_id: Literal["foo", "bar"]):
    return items[item_id]


@app.get("/items/{item_id}/public", response_model=Item)
async def read_item_bublic_data(item_id: Literal["foo", "bar"]):
    return items[item_id]
