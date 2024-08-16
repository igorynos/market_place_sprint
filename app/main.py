from concurrent.futures import wait, ThreadPoolExecutor

import uvicorn
from fastapi import FastAPI

from app import brocker  # noqa
from app.config import load_config
from routers import orders as OrderRouter
from routers import products as ProductRouter
from routers import shops as ShopRouter
from routers import users as UserRouter

config = load_config()

app = FastAPI()

app.include_router(UserRouter.router, prefix='/users')
app.include_router(ProductRouter.router, prefix='/product')
app.include_router(OrderRouter.router, prefix='/orders')
app.include_router(ShopRouter.router, prefix='/shops')


def start_app():
    uvicorn.run(app, host=config['uvicorn_host'], port=config['uvicorn_port'])


if __name__ == "__main__":
    executor = ThreadPoolExecutor(4)
    pool_list = [executor.submit(start_app), executor.submit(brocker.consumer.main)]
    try:
        wait(pool_list)
    except KeyboardInterrupt:
        print("Server is shutting down...")
    finally:
        executor.shutdown(wait=False)
