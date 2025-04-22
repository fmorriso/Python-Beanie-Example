import sys
from importlib.metadata import version

from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from models import Products
from program_settings import ProgramSettings


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
    await init_beanie(database = client.db_name, document_models = [Products])


def get_python_version() -> str:
    return f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"


def get_package_version(package_name: str) -> str:
    return version(package_name)

async def main():
    await init()

if __name__ == '__main__':
    print(f"Python version: {get_python_version()}")
    print(f"Beanie version: {get_package_version('beanie')}")
    print(f"Motor version: {get_package_version('motor')}")
    print(f"Pydantic version: {get_package_version('pydantic')}")
    main()

    # asyncio.run(init())
    #display_collections()
    # asyncio.run(read_products())
