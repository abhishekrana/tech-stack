import logging
from typing import Self

from app_1.internal.models.products import ProductDB


class ProductRepo:
    def __init__(self: Self) -> None:
        pass

    async def find(self: Self) -> list[ProductDB]:
        try:
            items: list[ProductDB] = await ProductDB.find_all().to_list()
            return items

        except Exception as e:
            logging.error(f"{e=!r}")
            raise e

    async def create(self: Self, items: list[ProductDB]) -> list[ProductDB]:
        try:
            for item in items:
                await item.create()
            return items  # TODO: return upated db items

        except Exception as e:
            logging.error(f"{e=!r}")
            raise e
