from dotenv import load_dotenv
from src.utils.common_logger import logger


def read_env_file(env_file_path: str):
    """
    Read environment variables from file
    """
    try:
        load_dotenv(dotenv_path=env_file_path)
    except Exception as err:
        logger.error(f"Fail to load configuration: {err}")
