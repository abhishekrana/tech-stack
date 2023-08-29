from pydantic import Field
from pydantic_settings import BaseSettings


class MongoDBConfig(BaseSettings):
    host: str = Field("127.0.0.1", alias="MONGODB_SVC_HOST")
    port: str = Field("27017", alias="MONGODB_SVC_PORT")
    database: str = Field("tech_stack_db", alias="MONGODB_SVC_DATABASE")
    user: str = Field("admin", alias="MONGODB_SVC_USER")
    password: str = Field("adminAdmin123!", alias="MONGODB_SVC_PASSWORD")  # TODO: use SecretStr


def load_mongodb_config() -> MongoDBConfig:
    return MongoDBConfig.model_construct(**MongoDBConfig().model_dump())  # pyright: ignore [reportGeneralTypeIssues]
