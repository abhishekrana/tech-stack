from pydantic import Field
from pydantic_settings import BaseSettings


class App1Config(BaseSettings):
    host: str = Field("127.0.0.1", validation_alias="APP_1_HOST")
    port: int = Field(5000, validation_alias="APP_1_PORT")
    reload: bool = Field(True, validation_alias="APP_1_RELOAD")


def load_app_1_config() -> App1Config:
    return App1Config.model_construct()
