# Goal: load from sqlite sakila into sakila.duckdb

import dlt
from dlt.sources.sql_database import sql_database
from pathlib import Path

DATA_PATH = Path(__file__).parent / "data"

print(DATA_PATH)


DUCKDB_PATH = Path(__file__).parent / "sakila.duckdb"

# source path
SQLITE_PATH = DATA_PATH / "sqlite-sakila.db"

# target path
DUCKDB_PATH = DATA_PATH / "sakila.duckdb"

source = sql_database(f"sqlite:///{SQLITE_PATH}", schema="main")

# pipeline writing to a DuckDB file
pipeline = dlt.pipeline(
    pipeline_name="sakila_sqlite_duckdb",
    destination=dlt.destinations.duckdb(str(DUCKDB_PATH)),
    dataset_name="staging",
)


# run the load (this captures ALL tables automatically)
load_info = pipeline.run(source, write_disposition="replace")

print(load_info)
