from typing import Any

from fastapi import Body
from fastapi.param_functions import Depends
from fastapi.routing import APIRouter
from sqlalchemy.orm.session import Session

from app_1.internal.models.users import UserCreateRequest, UserCreateResponse, UserFindResponse
from app_1.internal.repos.postgresql import get_session
from app_1.internal.repos.users import UserRepo
from app_1.internal.users.service import UserService

router: APIRouter = APIRouter()

example: list[dict[str, Any]] = [
    {
        "name": "mock-name",
        "fullname": "mock-fullname",
    }
]


@router.get(
    "/v1/users/",
    summary="Find users.",
    response_model=list[UserFindResponse],
)
def find(
    session: Session = Depends(get_session),
) -> list[UserFindResponse] | None:
    """Find users."""
    repo: UserRepo = UserRepo(session)
    service: UserService = UserService(repo)
    return service.find()


@router.post(
    "/v1/users/",
    summary="Create users.",
    response_model=list[UserCreateResponse],
)
def create(
    body: list[UserCreateRequest] = Body(example=example),
    session: Session = Depends(get_session),
) -> list[UserCreateResponse]:
    """Create users."""
    repo: UserRepo = UserRepo(session)
    service: UserService = UserService(repo)
    return service.create(body)
