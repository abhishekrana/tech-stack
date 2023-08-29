from pydantic import Field
from pydantic_settings import BaseSettings


class App1Config(BaseSettings):
    host: str = Field("0.0.0.0", alias="APP_1_HOST")
    port: int = Field(5000, alias="APP_1_PORT")
    reload: bool = Field(True, alias="APP_1_RELOAD")  # TODO: str not casted to bool


def load_app_1_config() -> App1Config:
    return App1Config.model_construct()
