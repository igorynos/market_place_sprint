import uvicorn
from fastapi import FastAPI

from app import models
from app.database import Base, engine

models = models

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

app = FastAPI()

if __name__ == "__main__":
    try:
        uvicorn.run(app, host='localhost', port=8000)
    except KeyboardInterrupt:
        print("Server is shutting down...")
