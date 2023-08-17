from datetime import datetime
from uuid import UUID

from pydantic import BaseModel
from sqlalchemy import func
from sqlalchemy.orm import DeclarativeBase, Mapped, MappedAsDataclass, mapped_column


# Database model
class Base(MappedAsDataclass, DeclarativeBase):
    pass


class UserDB(Base):
    __tablename__ = "users"
    id: Mapped[UUID] = mapped_column(primary_key=True, init=False)
    name: Mapped[str]
    fullname: Mapped[str | None]
    created_at: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now(), default=func.now()
    )  # TODO: server_default not working
    updated_at: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now(), default=func.now(), onupdate=func.now()
    )
    deleted_at: Mapped[datetime | None] = mapped_column(init=False, default=None)


# API models
class UserCreateRequest(BaseModel):
    name: str
    fullname: str


class UserCreateResponse(BaseModel):
    id: UUID
    name: str
    fullname: str
    created_at: datetime
    updated_at: datetime


class UserFindResponse(BaseModel):
    id: UUID
    name: str
    fullname: str
    created_at: datetime
    updated_at: datetime
