from typing import Union, Literal

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr, PydanticUserError

app = FastAPI()


class UserBase(BaseModel):
    username: str
    full_name: str = None
    email: EmailStr


class UserIn(UserBase):
    password: EmailStr


class UserOut(UserBase):
    pass


class UserInDB(UserBase):
    hashed_password: str


def fake_password_hasher(raw_password: str):
    return f"supersecret{raw_password}"


def fake_save_user(user_in: UserIn):
    hashed_password = fake_password_hasher(user_in.password)
    user_in_db = UserInDB(**user_in.model_dump(), hashed_password=hashed_password)
    print("User saved! ..not really")
    return user_in_db


@app.post("/user/", response_model=UserOut)
async def create_user(user_in: UserIn):
    user_saved = fake_save_user(user_in)
    return user_saved


class BaseItem(BaseModel):
    description: str
    type: str


# For overriding purpose: when a field defined on a base class was overridden by a non-annotated attribute.
"""
from pydantic import BaseModel, PydanticUserError

class BaseItem(BaseModel):
    description: str
    type: str
    try:

    class CarItem(BaseItem):
        type: str = "car"


    class PlaneItem(BaseItem):
        type: str = "plane"
        size: int
    except PydanticUserError as exc_info:
        assert exc_info.code == 'model-field-overridden'
"""


class CarItem(BaseItem):
    type: str = "car"


class PlaneItem(BaseItem):
    type: str = "plane"
    size: int


items = {
    "item1": {"description": "All my friends drive a low rider", "type": "car"},
    "item2": {
        "description": "Music was better in those days",
        "type": "plane",
        "size": 10,
    },
}


@app.get("/items/{item_id}", response_model=Union[CarItem, PlaneItem])
async def read_item(item_id: Literal["item1", "item2"]):
    return items[item_id]
