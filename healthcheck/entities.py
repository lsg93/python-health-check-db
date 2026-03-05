from dataclasses import dataclass

from healthcheck.base_entities import BaseEntity, HasCreatedAt, HasUuid


@dataclass(kw_only=True, slots=True)
class HealthCheck(BaseEntity, HasUuid, HasCreatedAt):
    service_name: str
    status: int  # Could be an Enum later.
