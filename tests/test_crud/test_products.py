from contextlib import nullcontext as does_not_raise

import pytest

from app.models.product import Products
from app.services.products import create_product
from tests.conftest import TestingSessionLocal


@pytest.mark.parametrize(
    'title, description, price',
    [
        ('goose', 'big goose', 500),
        ('goose', 'big goose', '500'),
        (111, 'big goose', '500'),
    ]
)
def test_product(title, description, price):
    with TestingSessionLocal() as db:
        product = Products(title=title,
                           description=description,
                           price=price,
                           )
        create_product(product, db)


@pytest.mark.parametrize('id', [id + 1 for id in range(3)])
def test_delete_product_id(add_client, id):
    response = add_client.delete(f'/product/{id}')
    assert response.status_code == 200


@pytest.mark.parametrize(
    'title, description, price, expectation',
    [
        ('goose', 'big goose', 500, does_not_raise()),
        ('goose', 'big goose', '500', does_not_raise()),
        (111, 'big goose', '500.7', pytest.raises(Exception)),
        ('goose', 'big goose', '500.gg', pytest.raises(Exception)),
    ]
)
def test_create_product(add_client, title, description, price, expectation):
    with expectation:
        response = add_client.post('/product/', json={
            "title": title,
            "description": description,
            "price": price
        })
        assert response.status_code == 200


@pytest.mark.parametrize('id', [id + 1 for id in range(4)])
def test_get_product_id(add_client, id):
    response = add_client.get(f'/product/{id}')
    assert response.status_code == 200


def test_check_type_product(add_client):
    response = add_client.get('/product/')
    products = response.json()
    for prod in products:
        assert type(prod['title']) == str
        assert type(prod['description']) == str
        assert type(prod['price']) == float


def test_get_prod():
    with TestingSessionLocal() as db:
        product_count = db.query(Products).count()
        assert product_count == 2
