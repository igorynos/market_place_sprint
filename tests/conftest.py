import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.config import load_config
from app.database import Base
from app.main import app
from app.models.order_status import Order_status

config = load_config()
SQLALCHEMY_URL = f"{config['db_engine']}+{config['db_driver']}://{config['db_user']}:{config['db_password']}@{config['db_host']}:{config['db_port']}/{config['db_name_tests']}"

engine_tests = create_engine(SQLALCHEMY_URL, echo=False)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine_tests)


@pytest.fixture(autouse=True, scope='session')
def add_database():
    Base.metadata.drop_all(engine_tests)
    Base.metadata.create_all(engine_tests)
    yield
    # Base.metadata.drop_all(engine_tests)


@pytest.fixture(autouse=True, scope='session')
def add_client():
    client = TestClient(app)
    yield client


@pytest.fixture(autouse=True, scope='session')
def add_status():
    for id in range(6):
        status = Order_status(title=f'status{id + 1}')
        try:
            TestingSessionLocal.add(status)
            TestingSessionLocal.commit()
            TestingSessionLocal.refresh(status)
        except Exception:
            pass
