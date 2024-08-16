from pydantic import BaseModel, Field


class Products(BaseModel):
    title: str
    description: str
    price: float = Field(ge=0)
