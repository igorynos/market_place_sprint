from pydantic import BaseModel, Field


class Orders(BaseModel):
    user_id: int
    shop_id: int
    product_id: int
    status_id: int | None = Field(None, exclude=True)
