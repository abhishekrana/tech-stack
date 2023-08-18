from pydantic import Field
from pydantic_settings import BaseSettings


class PostgresqlConfig(BaseSettings):
    host: str = Field("127.0.0.1", alias="POSTGRESQL_HOST")
    port: str = Field("5432", alias="POSTGRESQL_PORT")
    database: str = Field("tech_stack_db", alias="POSTGRESQL_DATABASE")
    user: str = Field("admin", alias="POSTGRESQL_USER")
    password: str = Field("adminAdmin123!", alias="POSTGRESQL_PASSWORD")  # TODO: use SecretStr
    echo: bool = Field(True, alias="POSTGRESQL_ECHO")  # TODO: str not casted to bool


def load_postgresql_config() -> PostgresqlConfig:
    return PostgresqlConfig.model_construct()