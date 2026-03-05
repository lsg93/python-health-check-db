from sqlalchemy.orm import registry

from healthcheck.entities import HealthCheck
from healthcheck.tables import healthcheck_table

mapper_registry = registry()

mapper_registry.map_imperatively(HealthCheck, healthcheck_table)
