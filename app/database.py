from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from app.config import load_config

config = load_config()
SQLALCHEMY_URL = f"{config['db_engine']}+{config['db_driver']}://{config['db_user']}:{config['db_password']}@{config['db_host']}:{config['db_post']}/{config['db_name']}"

engine = create_engine(SQLALCHEMY_URL, echo=False)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

Base.metadata.create_all(engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


if __name__ == '__main__':
    pass
