from datetime import datetime
from typing import Self

from app_1.internal.helpers.utils import get_timestamp, get_uuid
from app_1.internal.models.products import ProductCreateRequest, ProductCreateResponse, ProductDB, ProductFindResponse
from app_1.internal.repos.products import ProductRepo


class ProductService:
    def __init__(self: Self, repo: ProductRepo) -> None:
        self.repo: ProductRepo = repo

    async def find(self: Self) -> list[ProductFindResponse]:
        product_db: list[ProductDB] = await self.repo.find()
        product: list[ProductFindResponse] = [ProductFindResponse.model_validate(x) for x in product_db]
        return product

    async def create(self: Self, body: list[ProductCreateRequest]) -> list[ProductCreateResponse]:
        items: list[ProductDB] = []
        timestamp: datetime = get_timestamp()
        for item in body:
            items.append(
                ProductDB(
                    id=get_uuid(),
                    name=item.name,
                    description=item.description,
                    price=item.price,
                    created_at=timestamp,
                    updated_at=timestamp,
                    deleted_at=None,
                )
            )
        product_db: list[ProductDB] = await self.repo.create(items)
        product: list[ProductCreateResponse] = [ProductCreateResponse.model_validate(x) for x in product_db]
        return product
