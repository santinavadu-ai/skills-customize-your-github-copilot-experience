from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List

# Initialize the FastAPI application
app = FastAPI()

# Define data models using Pydantic
class Item(BaseModel):
    id: Optional[int] = None
    name: str
    description: Optional[str] = None

# Sample data store (in-memory database for simplicity)
items_db: List[Item] = [
    Item(id=1, name="Item 1", description="First sample item"),
    Item(id=2, name="Item 2", description="Second sample item"),
]

# TODO: Task 1 - Create Basic Endpoints
# Create a GET endpoint at "/" that returns a welcome message
# Create a GET endpoint at "/items" that returns all items


# TODO: Task 2 - Add Path and Query Parameters
# Create a GET endpoint at "/items/{item_id}" that returns a specific item
# Create a GET endpoint at "/search" that accepts a query parameter


# TODO: Task 3 - Handle POST Requests
# Create a POST endpoint at "/items" that accepts item data


# TODO: Task 4 - Add Error Handling
# Update endpoints to return appropriate status codes and error messages

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
