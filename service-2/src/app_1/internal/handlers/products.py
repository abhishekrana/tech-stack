from fastapi import status
from fastapi.routing import APIRouter

from app_1.internal.models.products import ProductCreateRequest, ProductCreateResponse, ProductFindResponse
from app_1.internal.products.service import ProductService
from app_1.internal.repos.products import ProductRepo

router: APIRouter = APIRouter()


@router.get(
    "/v1/products/",
    summary="Find products.",
    response_model=list[ProductFindResponse],
    status_code=status.HTTP_200_OK,
)
async def find() -> list[ProductFindResponse] | None:
    """Find products."""
    repo: ProductRepo = ProductRepo()
    service: ProductService = ProductService(repo)
    return await service.find()


@router.post(
    "/v1/products/",
    summary="Create products.",
    response_model=list[ProductCreateResponse],
    status_code=status.HTTP_201_CREATED,
)
async def create(
    body: list[ProductCreateRequest],
) -> list[ProductCreateResponse]:
    """Create products."""
    repo: ProductRepo = ProductRepo()
    service: ProductService = ProductService(repo)
    return await service.create(body)
