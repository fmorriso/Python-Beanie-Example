import os, sys
import asyncio
from typing import Optional

from dotenv import load_dotenv
from pymongo import MongoClient

from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel
from beanie import Document, Indexed, init_beanie


async def read_products():
    client = get_mongodb_client()
    print(f'{client=}')


def get_connection_string() -> str:
    load_dotenv()

    template: str = os.environ.get('mongodb_connection_template')
    uid: str = os.environ.get('mongodb_uid')
    pwd: str = os.environ.get('mongodb_pwd')

    return f'mongodb+srv://{uid}:{pwd}@{template}'


def get_mongodb_client() -> AsyncIOMotorClient:
    # print(f'{get_connection_string()=}')
    return AsyncIOMotorClient(get_connection_string())


def get_python_version() -> str:
    return f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"


if __name__ == '__main__':
    print(f"Python version: {get_python_version()}")

    asyncio.run(read_products())
