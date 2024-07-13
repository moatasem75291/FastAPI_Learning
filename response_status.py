from fastapi import FastAPI, status

app = FastAPI()

"""
The status_code parameter is used to set the status code of the response.
The default status code is 200 OK.

"""


@app.post("/items", status_code=status.HTTP_201_CREATED)
async def create_item(name: str):
    return {"name": name}


@app.delete("/items/{pk}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_item(pk: str):
    print(f"Item '{pk}' has been deleted..!")
    return pk


@app.get("/items/", status_code=status.HTTP_301_MOVED_PERMANENTLY)
async def read_items_redirect():
    return {"message": "Bye World!!"}
