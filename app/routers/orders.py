import json

from fastapi import APIRouter

from app.brocker.producer import message_orders
from app.dto.orders import Orders as OrdersDTO

router = APIRouter()


@router.post('/', tags=['order'])
async def create(data: OrdersDTO):
    body = data.json()
    message_orders('orders', 'new_orders', body=body)
    return data


