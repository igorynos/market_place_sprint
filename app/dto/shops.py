from pydantic import BaseModel


class Shops(BaseModel):
    name: str
    description: str
    email: str
    phone_number: str
