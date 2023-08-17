import logging
from typing import Self

from fastapi import status
from sqlalchemy import select
from sqlalchemy.exc import DBAPIError
from sqlalchemy.orm.session import Session

from app_1.internal.helpers.app_errors import AppError, AppErrorType
from app_1.internal.helpers.utils import get_uuid
from app_1.internal.models.users import UserDB


class UserRepo:
    def __init__(self: Self, session: Session) -> None:
        self.session: Session = session

    def find(self: Self) -> list[UserDB]:
        try:
            # stmt = select(UserDB.name)
            # items: list[UserDB] = self.session.execute(stmt)
            # return items
            stmt = select(UserDB).where(UserDB.deleted_at.is_(None))
            items: list[UserDB] = self.session.scalars(stmt)
            # items: list[UserDB] = (
            #     self.session.select(UserDB)
            #     .where(UserDB.deleted_at == None)
            #     .all()  # pylint: disable=singleton-comparison
            # )
            return items

        except Exception as e:
            logging.error(f"{e=!r}")
            raise e

    def create(self: Self, items: list[UserDB]) -> list[UserDB]:
        try:
            for item in items:
                if item.id is None:
                    item.id = get_uuid()
                self.session.add(item)
                self.session.commit()
                self.session.refresh(item)

        except DBAPIError as e:
            if AppErrorType.ERROR_UNIQUE_CONSTRAINT.value in e.orig.args[0].get("M"):
                raise AppError(
                    AppErrorType.ERROR_UNIQUE_CONSTRAINT,
                    detail="" if len(e.orig.args) == 0 else e.orig.args[0].get("D"),
                    status_code=status.HTTP_400_BAD_REQUEST,
                ) from e
            logging.error(f"{e=!r}")
            raise e

        except Exception as exc:
            logging.error(f"Exception: {exc}")
            raise exc

        return items
