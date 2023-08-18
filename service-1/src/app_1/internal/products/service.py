from typing import Self

from app_1.internal.helpers.utils import get_uuid
from app_1.internal.models.products import ProductCreateRequest, ProductCreateResponse, ProductDB, ProductFindResponse
from app_1.internal.repos.products import ProductRepo


class ProductService:
    def __init__(self: Self, repo: ProductRepo) -> None:
        self.repo: ProductRepo = repo

    async def find(self: Self) -> list[ProductFindResponse]:
        user_db: list[ProductDB] = await self.repo.find()
        user: list[ProductFindResponse] = [ProductFindResponse.model_validate(x) for x in user_db]
        return user

    async def create(self: Self, body: list[ProductCreateRequest]) -> list[ProductCreateResponse]:
        items: list[ProductDB] = []
        for item in body:
            items.append(
                ProductDB(
                    id=get_uuid(),
                    name=item.name,
                    description=item.description,
                    price=item.price,
                )
            )
        user_db: list[ProductDB] = await self.repo.create(items)
        user: list[ProductCreateResponse] = [ProductCreateResponse.model_validate(x) for x in user_db]
        return user
