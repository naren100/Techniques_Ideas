# secondary.py
import json
from typing import Optional
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

@router.post("/items/")   # POST http://127.0.0.1:8000/items/
async def create_item(item: Item):
    # Pydantic v2 uses model_dump(); fall back to dict() for v1
    try:
        data = item.model_dump()
    except AttributeError:
        data = item.dict()

    # Pretty-print JSON to the server console
    print("SERVER RECEIVED:\n", json.dumps(data, indent=2, ensure_ascii=False))
    return item


