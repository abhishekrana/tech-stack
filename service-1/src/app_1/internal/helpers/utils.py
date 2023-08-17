import uuid
from uuid import UUID


def get_uuid() -> UUID:
    return uuid.uuid4()
