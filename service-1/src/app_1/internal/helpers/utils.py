import uuid
from datetime import datetime, timezone
from uuid import UUID


def get_timestamp() -> datetime:
    return datetime.now(tz=timezone.utc)


def get_uuid() -> UUID:
    return uuid.uuid4()
