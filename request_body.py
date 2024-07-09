from pydantic import BaseModel

from fastapi import FastAPI, Query, Path


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


@app.get("/items")
async def read_items(q: str = Query(..., min_length=3, max_length=12)):
    result = {
        "items": [
            {"item_id": 1, "name": "item1"},
            {"item_id": 2, "name": "item2"},
        ]
    }
    if q:
        result.update({"q": q})
    return result


@app.get("/items_validation/{item_id}")
async def read_items_validation(
    item_id: int = Path(..., title="This is the item ID ://"),
    size: float = Query(..., gt=0, le=7.25),
    q: str | None = Query(None, title="Put your query her ://", alias="item-query"),
):
    results = {
        "item_id": item_id,
        "size": size,
    }
    if q:
        results.update({"q": q})
    return results
