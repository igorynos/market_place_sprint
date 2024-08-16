import os

from dotenv import load_dotenv


def load_config():
    load_dotenv()
    config = {
        'db_engine': os.getenv('DB_ENGINE'),
        'db_driver': os.getenv('DB_DRIVER'),
        'db_name': os.getenv('DB_NAME'),
        'db_name_tests': os.getenv('DB_NAME_TESTS'),
        'db_user': os.getenv('DB_USER'),
        'db_password': os.getenv('DB_PASSWORD'),
        'db_host': os.getenv('DB_HOST'),
        'db_port': int(os.getenv('DB_PORT')),
        'rmq_host': os.getenv('RMQ_HOST'),
        'rmq_port': int(os.getenv('RMQ_PORT')),
        'uvicorn_host': os.getenv('UVICORN_HOST'),
        'uvicorn_port': int(os.getenv('UVICORN_PORT')),
    }
    return config
