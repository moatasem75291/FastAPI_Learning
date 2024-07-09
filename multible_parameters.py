from pydantic import BaseModel

from fastapi import FastAPI, Path, Query, Body

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


class User(BaseModel):
    username: str
    full_name: str | None = None


@app.put("/items/{item_id}")
async def update_items(
    *,
    item_id: int = Path(..., title="This is the Id for the Item.", ge=0, le=100),
    q: str | None = None,
    item: Item | None = Body(..., embed=True),
    user: User | None = Body(..., embed=True),
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})
    if user:
        results.update({"user": user})
    return results
