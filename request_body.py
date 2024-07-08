from pydantic import BaseModel

from fastapi import FastAPI  # type:ignore


app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@app.post("/items")
async def create_item(item: Item):
    item_dect = item.dict()
    if item_dect.get("tax", None):
        total = item_dect.get("price") + item_dect.get("tax")
        item_dect.update({"total": total})

    return item_dect


@app.put("/items/{item_id}")
async def create_item_with_put(item_id: int, item: Item, q: str | None = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result
