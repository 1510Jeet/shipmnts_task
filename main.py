from fastapi import FastAPI

# Create an instance of the FastAPI class
app = FastAPI()

# Define a path operation decorator
@app.get("/")
def read_root():
    """
    This endpoint returns a welcome message.
    """
    return {"Hello": "World"}

# Another example endpoint
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    """
    This endpoint takes a path parameter `item_id` and an optional
    query parameter `q`.
    """
    return {"item_id": item_id, "q": q}