import logging

from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient  # type: ignore

from app_1.internal.configs.mongodb import MongoDBConfig, load_mongodb_config
from app_1.internal.models.products import ProductDB


async def init_mongodb() -> None:
    config: MongoDBConfig = load_mongodb_config()
    logging.info(f"Connecting to mongodb://{config.user}:*****@{config.host}:{config.port}/{config.database}")
    print(f"Connecting to mongodb://{config.user}:*****@{config.host}:{config.port}/{config.database}")

    client = AsyncIOMotorClient(f"mongodb://{config.user}:{config.password}@{config.host}:{config.port}")

    await init_beanie(
        database=client.db_name,
        document_models=[  # type: ignore
            ProductDB,
        ],
    )
