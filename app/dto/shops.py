from pydantic import BaseModel, constr, EmailStr, validator


class Shops(BaseModel):
    name: constr(min_length=1, max_length=30)
    description: str
    email: EmailStr
    phone_number: str

    @validator('phone_number')
    def validate_phone(cls, value):
        if '+' not in value:
            raise ValueError('Phone number must include a "+" symbol')
        return value



