from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient  # type: ignore

from app_1.internal.configs.mongodb import MongoDBConfig, load_mongodb_config
from app_1.internal.models.products import ProductDB


async def init_mongodb() -> None:
    config: MongoDBConfig = load_mongodb_config()

    client = AsyncIOMotorClient(f"mongodb://{config.user}:{config.password}@{config.host}:{config.port}")

    await init_beanie(
        database=client.db_name,
        document_models=[  # type: ignore
            ProductDB,
        ],
    )
