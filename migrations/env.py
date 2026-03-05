import os
from logging.config import fileConfig

from alembic import context
from sqlalchemy import create_engine, pool

# 1. Import your Metadata and Tables here
# As a Platform Engineer, remember to import the tables so they register!
from database.metadata import metadata

print(f"ALEMBIC DEBUG: Detected tables: {list(metadata.tables.keys())}")

# This is the Alembic Config object, which has access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Set the target metadata for 'autogenerate' support
target_metadata = metadata


def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""

    # 2. Grab the URL from the environment (populated by uv --env-file)
    database_url = os.getenv("PYTHON_DBAPI")

    if not database_url:
        raise RuntimeError(
            "PYTHON_DBAPI not found! Make sure you run with: "
            "uv run --env-file .env alembic ..."
        )

    # 3. Create the engine directly from the environment string
    # We bypass 'engine_from_config' to avoid KeyError 'url'
    connectable = create_engine(
        database_url,
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            # This ensures Postgres schemas are handled correctly
            compare_type=True,
        )

        with context.begin_transaction():
            context.run_migrations()


# Standard Alembic entry points
if context.is_offline_mode():
    # If you ever need to generate raw SQL scripts
    context.configure(url=os.getenv("PYTHON_DBAPI"), target_metadata=target_metadata)
    with context.begin_transaction():
        context.run_migrations()
else:
    run_migrations_online()
