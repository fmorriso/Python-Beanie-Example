import asyncio
import sys
from importlib.metadata import version

from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from models import Products
from program_settings import ProgramSettings
from datetime import datetime, timezone


def get_python_version() -> str:
    return f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"


def get_package_version(package_name: str) -> str:
    return version(package_name)

def get_current_datetime() -> str:
    # Get the current UTC time
    current_gmt = datetime.now(timezone.utc)

    # Format the output to include fractional seconds to 2 decimal places
    formatted_gmt = f"{current_gmt.year}-{current_gmt.month:02d}-{current_gmt.day:02d} " \
                    f"{current_gmt.hour:02d}:{current_gmt.minute:02d}:{current_gmt.second:02d}." \
                    f"{current_gmt.microsecond // 10000:02d}"

    return formatted_gmt


async def read_products():
    client = get_client()
    print(f'{client=}')
    db = client['store']
    print(f'{db.name=}')
    await init_beanie(database = db, document_models = [Products])
    print('init_beanie completed')


def get_connection_string() -> str:
    template: str = ProgramSettings.get_setting('MONGODB_CONNECTION_TEMPLATE')
    uid: str = ProgramSettings.get_setting('MONGODB_UID')
    pwd: str = ProgramSettings.get_setting('MONGODB_PWD')

    return f'mongodb+srv://{uid}:{pwd}@{template}'


def get_client() -> AsyncIOMotorClient:
    return AsyncIOMotorClient(get_connection_string())


async def init():
    # Create Motor client
    client = AsyncIOMotorClient("mongodb://user:pass@host:27017")

    # Init beanie with the Product document class
    print(f'before init_beanie: {get_current_datetime()}')
    await init_beanie(database = client.db_name, document_models = [Products])
    print(f'after  init_beanie: {get_current_datetime()}')


async def main():
    await init()


if __name__ == '__main__':
    print(f"Python version: {get_python_version()}")
    print(f"Beanie version: {get_package_version('beanie')}")
    print(f"Motor version: {get_package_version('motor')}")
    print(f"Pydantic version: {get_package_version('pydantic')}")
    asyncio.run(main())

    # asyncio.run(init())
    # display_collections()
    # asyncio.run(read_products())
