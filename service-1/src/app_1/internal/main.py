import logging

import uvicorn
from fastapi import FastAPI

from app_1.internal.configs.app_1 import App1Config, load_app_1_config
from app_1.internal.handlers import health

logging.basicConfig(level=logging.INFO)

app: FastAPI = FastAPI()

app.include_router(health.router, tags=["Health"])

if __name__ == "__main__":
    config: App1Config = load_app_1_config()
    print(f"{config=}")

    uvicorn.run(
        "main:app",
        host=config.host,
        port=config.port,
        reload=config.reload,
    )
