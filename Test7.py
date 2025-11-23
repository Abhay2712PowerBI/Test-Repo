from typing import List
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import os


class Customer(BaseModel):
    id: int
    name: str


app = FastAPI(title="Customer API", version="0.1")

# CORS - permissive for development; lock this down for production
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


_CUSTOMERS = [
    {"id": 1, "name": "John Doe"},
    {"id": 2, "name": "Jane Smith"},
    {"id": 3, "name": "Alice Johnson"},
]


@app.get("/customers", response_model=List[Customer], summary="List customers")
async def get_customers() -> List[Customer]:
    """Return a list of customers.

    Currently returns in-memory sample data. Replace with a database
    or external data source as needed.
    """
    return _CUSTOMERS


if __name__ == "__main__":
    # Allow running the app locally for quick testing
    import uvicorn

    uvicorn.run("Test7:app", host="127.0.0.1", port=int(os.getenv("PORT", 8000)), reload=True)
