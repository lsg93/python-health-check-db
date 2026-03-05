import datetime
from dataclasses import dataclass, field
from typing import Optional
from uuid import UUID, uuid4


@dataclass(kw_only=True)
class BaseEntity:
    id: Optional[int] = None


@dataclass(kw_only=True)
class HasCreatedAt:
    created_at: datetime = field(
        default_factory=lambda: datetime.now(datetime.timezone.utc)
    )


@dataclass(kw_only=True)
class HasUpdatedAt:
    updated_at: datetime = field(
        default_factory=lambda: datetime.now(datetime.timezone.utc)
    )


@dataclass(kw_only=True, slots=True)
class HasUuid:
    uuid: UUID = field(default_factory=uuid4)
