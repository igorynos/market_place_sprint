from contextlib import nullcontext as does_not_raise

import pytest
from pydantic import ValidationError

from app.dto.shops import Shops as DTOShops
from app.models.shops import Shops
from app.services.shops import create_shop
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


@pytest.mark.parametrize('name, description, email, phone_number, status, expectation', data_test)
def test_shops(name, description, email, phone_number, status, expectation):
    with TestingSessionLocal() as db:
        with expectation:
            shop_data = {
                "name": name,
                "description": description,
                "email": email,
                "phone_number": phone_number
            }
            DTOShops(**shop_data)
            shop = Shops(**shop_data)
            create_shop(shop, db)


@pytest.mark.parametrize('id', [id + 1 for id in range(2)])
def test_delete_shop_id(add_client, id):
    response = add_client.delete(f'/shops/{id}')
    assert response.status_code == 200


@pytest.mark.parametrize('name, description, email, phone_number, status, expectation', data_test)
def test_create_shop(add_client, name, description, email, phone_number, status, expectation):
    response = add_client.post('/shops/', json={
            "name": name,
            "description": description,
            "email": email,
            "phone_number": phone_number
        })
    assert response.status_code == status


@pytest.mark.parametrize('id', [id + 1 for id in range(2)])
def test_get_shop_id(add_client, id):
    response = add_client.get(f'/shops/{id}')
    assert response.status_code == 200


def test_check_type_shop(add_client):
    response = add_client.get('/shops/')
    products = response.json()
    for prod in products:
        assert type(prod['name']) == str
        assert type(prod['description']) == str
        assert type(prod['email']) == str
        assert type(prod['phone_number']) == str


def test_get_shop():
    with TestingSessionLocal() as db:
        shops_count = db.query(Shops).count()
        assert shops_count == 2
