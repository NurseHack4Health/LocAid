import os
import sys

sys.path.insert(0, os.getcwd())
from sqlalchemy import MetaData
from sqlalchemy.schema import CreateSchema
from sqlalchemy_utils import database_exists, create_database
from src.utils.common_logger import logger
from src.data_layer.db_connector import engine
from src.data_layer.db_tables import BaseTable


class DBInitializer:
    def __init__(self):
        self.engine = engine
        self.BaseTable = MetaData()
        for (table_name, table) in BaseTable.metadata.tables.items():
            self.BaseTable._add_table(table_name, table.schema, table)

    def create_database(self):
        """
        Create database if it does not exist
        :return success: True if it succeeded or if database already exists
        """
        # Create database if it does not exist
        try:
            if database_exists(self.engine.url):
                logger.info("Database already exists. Skipping")
            create_database(self.engine.url)
        except Exception as err:
            logger.info(f"Failed to create database: {err}")

    def create_schema(self):
        """
        Create database schema
        """
        try:
            schema_name = os.environ.get('SCHEMA_NAME')
            if not schema_name:
                raise Exception(f"schema name not given")
            # Create schema
            self.engine.execute(CreateSchema(schema_name))
        except Exception as err:
            logger.info(f"Failed to create database: {err}")

    def create_tables(self):
        """
        Create database tables based on ORM models
        """
        self.BaseTable.create_all(self.engine)


if __name__ == '__main__':
    DBI = DBInitializer()
    DBI.create_database()
    DBI.create_schema()
    DBI.create_tables()
