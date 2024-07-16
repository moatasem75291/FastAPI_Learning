from enum import Enum

from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None
    tags: set[str] = set()


class Tags(Enum):
    item = "item"
    user = "user"


@app.post(
    "/items/",
    status_code=status.HTTP_201_CREATED,
    response_model=Item,
    summary="Create an item",
    # description="Create an item with all the information, name, description, price, tax and tags",
    tags=[Tags.item],
)
def create_item(item: Item):
    """
    Create an item with all the information:
    - **name**: each item must have a name
    - **description**: a long description
    - **price**: required
    - **tax**: if the item doesn't have tax, you can omit it
    - **tags**: a set of unique tag strings for this item
    - **tags**: a set of unique tag strings for this item

    """
    return item
