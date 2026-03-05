from sqlalchemy import Column, Integer, String, Table, Uuid

from database.metadata import metadata

healthcheck_table = Table(
    "healthcheck",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("uuid", Uuid, nullable=False, unique=True),
    Column("service_name", String),
    Column("status", Integer),
)
