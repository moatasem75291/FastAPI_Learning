from fastapi import FastAPI, Body

from pydantic import BaseModel, Field

app = FastAPI()

url_regex = r"https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()!@:%_\+.~#?&\/\/=]*)"


class Image(BaseModel):
    url: str = Field(..., pattern=url_regex)
    name: str


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[int] = []
    image: Image | None = None


class offers(BaseModel):
    name: str
    description: str | None = None
    price: float
    items: list[Item]


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results


@app.put("/offers")
async def create_offer(offer: offers = Body(..., embed=True)):
    return offer


@app.post("/images/multible")
async def create_multible_images(images: list[Image]):
    return images
