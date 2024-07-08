from fastapi import FastAPI  # type:ignore

app = FastAPI()


fake_items_db = [
    {"item_name": "Foo"},
    {"item_name": "Bar"},
    {"item_name": "Baz"},
]


@app.get("/items")
async def list_of_items(skip: int = 0, limit: int = 10):
    return {"results": fake_items_db[skip : skip + limit]}


# Now let's try to use Optional query parameters.
@app.get("/items/{item_id}")
async def get_item(item_id: int, q: str | None = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}


# Hmmm, What about the type cnversions!!
@app.get("/items_desc/{item_id}")
async def get_item_with_desc(item_id: int, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item


# What if you want to sent a multible required parameters in the URL.
@app.get("/items/{item_id}/name/{item_name}")
async def get_item_name(
    item_id: int, item_name: str, q: str | None = None, short: bool = False
):
    item = {"item_name": item_name, "item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item
