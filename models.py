import asyncio
from typing import Optional

from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel


class Products(BaseModel):
    id: int
    name: str
    price: float
    category: str
    image: str
