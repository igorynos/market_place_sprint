import os

from dotenv import load_dotenv


def load_config():
    load_dotenv()
    config = {
        'db_engine': os.getenv('DB_ENGINE'),
        'db_driver': os.getenv('DB_DRIVER'),
        'db_name': os.getenv('DB_NAME'),
        'db_user': os.getenv('DB_USER'),
        'db_password': os.getenv('DB_PASSWORD'),
        'db_host': os.getenv('DB_HOST'),
        'db_post': os.getenv('DB_PORT'),
    }
    return config
