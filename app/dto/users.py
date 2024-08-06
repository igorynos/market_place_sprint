from pydantic import BaseModel


class Users(BaseModel):
    first_name: str
    second_name: str
    email: str
    phone_number: str
