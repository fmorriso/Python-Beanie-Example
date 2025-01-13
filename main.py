import os, sys
import asyncio
from typing import Optional

from dotenv import load_dotenv
from pymongo import MongoClient

from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel
from beanie import Document, Indexed, init_beanie

from models import Products


async def read_products():
    client = get_client()
    print(f'{client=}')
    db = client['store']
    print(f'{db.name=}')
    await init_beanie(database=db, document_models=[Products])
    print('init_beanie completed')


def get_connection_string() -> str:
    load_dotenv()

    template: str = os.environ.get('mongodb_connection_template')
    uid: str = os.environ.get('mongodb_uid')
    pwd: str = os.environ.get('mongodb_pwd')

    return f'mongodb+srv://{uid}:{pwd}@{template}'


def get_client() -> AsyncIOMotorClient:
    return AsyncIOMotorClient(get_connection_string())

async def init():
    # Create Motor client
    client = AsyncIOMotorClient("mongodb://user:pass@host:27017")

    # Init beanie with the Product document class
    await init_beanie(database=client.db_name, document_models=[Products])


def get_python_version() -> str:
    return f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"


if __name__ == '__main__':
    print(f"Python version: {get_python_version()}")
    asyncio.run(init())
    #display_collections()
    # asyncio.run(read_products())
