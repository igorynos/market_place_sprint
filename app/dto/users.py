from pydantic import BaseModel, validator, EmailStr, constr


class Users(BaseModel):
    first_name: constr(min_length=1, max_length=30)
    second_name: constr(min_length=1, max_length=30)
    email: EmailStr
    phone_number: str

    @validator('phone_number')
    def validate_phone(cls, value):
        if '+' not in value:
            raise ValueError('Phone number must include a "+" symbol')
        return value
