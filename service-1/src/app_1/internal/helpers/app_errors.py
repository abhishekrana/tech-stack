from enum import Enum
from typing import Self

from fastapi import status


class AppErrorType(Enum):
    # Service
    ERROR_USER_ID_DOES_NOT_EXIST = "user id does not exist"
    # Database
    ERROR_UNIQUE_CONSTRAINT = "duplicate key value violates unique constraint"


class AppError(Exception):
    def __init__(
        self: Self,
        type_: AppErrorType,
        detail: str | None = None,
        status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR,
    ) -> None:
        super().__init__()
        self.type: AppErrorType = type_
        self.detail: str | None = detail
        self.status_code: int = status_code
