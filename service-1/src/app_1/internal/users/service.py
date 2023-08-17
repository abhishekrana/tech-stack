from dataclasses import asdict
from typing import Self

from app_1.internal.models.users import UserCreateRequest, UserCreateResponse, UserDB, UserFindResponse
from app_1.internal.repos.users import UserRepo


class UserService:
    def __init__(self: Self, repo: UserRepo) -> None:
        self.repo: UserRepo = repo

    def find(self: Self) -> list[UserFindResponse]:
        user_db: list[UserDB] = self.repo.find()
        user: list[UserFindResponse] = [UserFindResponse.model_validate(asdict(x)) for x in user_db]
        return user

    def create(self: Self, body: list[UserCreateRequest]) -> list[UserCreateResponse]:
        items: list[UserDB] = []
        for item_body in body:
            items.append(
                UserDB(
                    name=item_body.name,
                    fullname=item_body.fullname,
                )
            )
        user_db: list[UserDB] = self.repo.create(items)
        user: list[UserCreateResponse] = [UserCreateResponse.model_validate(asdict(x)) for x in user_db]
        return user
