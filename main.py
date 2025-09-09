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

