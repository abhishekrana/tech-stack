import logging

import uvicorn
from fastapi import FastAPI

from app_1.internal.configs.app_1 import App1Config, load_app_1_config
from app_1.internal.handlers import health, users

logging.basicConfig(level=logging.DEBUG)

app: FastAPI = FastAPI(title="Tech Stack", description="Technology stack")

app.include_router(health.router, tags=["Health"])
app.include_router(users.router, tags=["Users"])

if __name__ == "__main__":
    config: App1Config = load_app_1_config()
    print(f"{config=}")

    uvicorn.run(  # pyright: ignore
        "main:app",
        host=config.host,
        port=config.port,
        reload=config.reload,
    )
