from fastapi import FastAPI, HTTPException, Request, status
from fastapi.responses import JSONResponse, PlainTextResponse
from fastapi.exceptions import RequestValidationError

app = FastAPI()

items = {
    1: {"name": "Item1"},
    2: {"name": "Item2"},
    3: {"name": "Item3"},
    4: {"name": "Item4"},
    5: {"name": "Item5"},
}


# 1st way
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    if item_id not in items:
        raise HTTPException(
            status_code=404,
            detail="Item not found",
            headers={"X-Error": "There goes my error"},
        )
    return {"name": items[item_id]["name"]}


# 2nd way


class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name


@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request: Request, exc: UnicornException):
    return JSONResponse(
        status_code=418,
        content={"message": f"Oops! {exc.name} did something. There goes a rainbow..."},
    )


@app.get("/unicorns/{name}")
async def read_unicorn(name: str):
    if name == "yolo":
        raise UnicornException(name=name)
    return {"unicorn_name": name}


# Let's repeat the 2nd way again paleeeeez.🥺


@app.exception_handler(RequestValidationError)
async def validation_excwption_handler(request: Request, exc: RequestValidationError):
    return PlainTextResponse(
        f"Oops! Something went wrong, Check it out:\n {str(exc)}", status_code=400
    )


@app.get("/validation_item/{item_id}")
async def validation_item(item_id: int):
    if item_id == 3:
        raise HTTPException(
            status_code=418,
            detail="Nope I don't like 3.",
            headers={"X-Error": "There goes my error"},
        )
    elif item_id not in items:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item not found"
        )

    return {"name": items[item_id]["name"]}
