from sqlalchemy.orm import Session

from app.dto import products
from app.models.product import Products


def create_product(data: products.Products, db):
    product = Products(title=data.title,
                    description=data.description,
                    price=data.price,
                    )

    try:
        db.add(product)
        db.commit()
        db.refresh(product)
    except Exception as error:
        print(error)

    return product


def get_product(id: int, db):
    return db.query(Products).filter(Products.id == id).first()


def update(data: products.Products, db: Session, id: int):
    product = db.query(Products).filter(Products.id == id).first()

    for params in data:
        product.params = params

    try:
        db.add(product)
        db.commit()
        db.refresh(product)
    except Exception as error:
        print(error)

    return product


def remove(id: int, db: Session):
    product = db.query(Products).filter(Products.id == id).delete()
    db.commit()
    return product
