from contextlib import nullcontext as does_not_raise

import pytest
from pydantic import ValidationError

from app.dto.users import Users as DTOUsers
from app.models.users import Users
from app.services.shops import create_shop
from app.services.users import create_user
from tests.conftest import TestingSessionLocal

data_test = [
    pytest.param('Goose', 'Big Goosesss', 'goose@example.com', '+1234567890', 200, does_not_raise()),  # корректные данные
    pytest.param('Duck', 'Small Duck', 'duck@example.com', '+0987654321', 200, does_not_raise()),  # корректные данные
    pytest.param('', 'No Name', 'empty@example.com', '0000000000', 422, pytest.raises(ValidationError)),  # пустое имя
    pytest.param('LongName' * 10, 'Very Long Description', 'longname@example.com', '1234567890', 422,
                 pytest.raises(ValidationError)),  # длинное имя
    pytest.param('Name', 'Description', 'invalid-email', '1234567890', 422, pytest.raises(ValidationError)),
    # некорректный email
    pytest.param('Name', 'Description', 'email@example.com', 'not-a-phone', 422, pytest.raises(ValidationError))
    # некорректный телефон
]


@pytest.mark.parametrize('first_name, second_name, email, phone_number, status, expectation', data_test)
def test_users(first_name, second_name, email, phone_number, status, expectation):
    with TestingSessionLocal() as db:
        with expectation:
            user_data = {
                "first_name": first_name,
                "second_name": second_name,
                "email": email,
                "phone_number": phone_number
            }
            DTOUsers(**user_data)
            user = Users(**user_data)
            create_user(user, db)


@pytest.mark.parametrize('id', [id + 1 for id in range(2)])
def test_delete_user_id(add_client, id):
    response = add_client.delete(f'/users/{id}')
    assert response.status_code == 200


@pytest.mark.parametrize('first_name, second_name, email, phone_number, status, expectation', data_test)
def test_create_users(add_client, first_name, second_name, email, phone_number, status, expectation):
    response = add_client.post('/users/', json={
            "first_name": first_name,
            "second_name": second_name,
            "email": email,
            "phone_number": phone_number
        })
    assert response.status_code == status


@pytest.mark.parametrize('id', [id + 1 for id in range(2)])
def test_get_user_id(add_client, id):
    response = add_client.get(f'/users/{id}')
    assert response.status_code == 200


def test_check_type_user(add_client):
    response = add_client.get('/users/')
    products = response.json()
    for prod in products:
        assert type(prod['first_name']) == str
        assert type(prod['second_name']) == str
        assert type(prod['email']) == str
        assert type(prod['phone_number']) == str


def test_get_user():
    with TestingSessionLocal() as db:
        shops_count = db.query(Users).count()
        assert shops_count == 2
