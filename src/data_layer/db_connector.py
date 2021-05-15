import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from src.utils.common_logger import logger
from src.utils.config_reader import read_env_file

# Setup DB connector
read_env_file('.env')

engine = create_engine(f"postgresql://{os.environ.get('DB_USER')}@{os.environ.get('DB_HOST')}:{os.environ.get('DB_PASSWORD')}@locaid.postgres.database.azure.com:{os.environ.get('DB_PORT')}/{os.environ.get('DB_NAME')}")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    try:
        db = SessionLocal()
        yield db
    except Exception as err:
        logger.error(f"Failed to connect to database: {err}")
    finally:
        db.close()
