from pydantic import Field
from pydantic_settings import BaseSettings


class PostgresqlConfig(BaseSettings):
    host: str = Field("127.0.0.1", alias="POSTGRESQL_SVC_HOST")
    port: str = Field("5432", alias="POSTGRESQL_SVC_PORT")
    database: str = Field("tech_stack_db", alias="POSTGRESQL_SVC_DATABASE")
    user: str = Field("admin", alias="POSTGRESQL_SVC_USER")
    password: str = Field("adminAdmin123!", alias="POSTGRESQL_SVC_PASSWORD")  # TODO: use SecretStr
    echo: bool = Field(True, alias="POSTGRESQL_SVC_ECHO")  # TODO: str not casted to bool


def load_postgresql_config() -> PostgresqlConfig:
    return PostgresqlConfig.model_construct(
        **PostgresqlConfig().model_dump()  # pyright: ignore [reportGeneralTypeIssues]
    )
