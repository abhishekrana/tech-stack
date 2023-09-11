import uuid
from datetime import datetime, timezone
from uuid import UUID

import pymongo
from beanie import Document, Indexed
from pydantic import BaseModel, ConfigDict, Field


# Database model
class ProductDB(Document):
    id: UUID = Field(default_factory=uuid.uuid4)
    name: str
    # name: Indexed(str, unique=True)
    description: str | None = None
    # description: Indexed(str, index_type=pymongo.TEXT)
    price: Indexed(float, index_type=pymongo.DESCENDING)  # pyright: ignore
    created_at: datetime = datetime.now(tz=timezone.utc)
    updated_at: datetime = datetime.now(tz=timezone.utc)
    deleted_at: datetime | None

    class Settings:
        name: str = "products"  # collection/database name
        # indexes: list[tuple[str, Any]] = [
        #     [
        #         ("name", pymongo.TEXT),
        #         ("description", pymongo.TEXT),
        #     ],
        # ]


# API models
class ProductCreateRequest(BaseModel):
    name: str
    description: str
    price: float

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "name": "mock-name",
                "description": "mock-description",
                "price": 3.14,
            }
        },
    )


class ProductCreateResponse(BaseModel):
    id: UUID
    name: str
    description: str
    price: float
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(
        from_attributes=True,
    )


class ProductFindResponse(BaseModel):
    id: UUID
    name: str
    description: str
    price: float
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(
        from_attributes=True,
    )
