from sqlalchemy.orm import Session

from app.dto import shops
from app.models.shops import Shops


def create_shop(data: shops.Shops, db):
    shop = Shops(name=data.name,
                 description=data.description,
                 email=data.email,
                 phone_number=data.phone_number,
                 )

    try:
        db.add(shop)
        db.commit()
        db.refresh(shop)
    except Exception as error:
        print(error)

    return shop


def get_shop(id: int, db):
    return db.query(Shops).filter(Shops.id == id).first()


def update(data: shops.Shops, db: Session, id: int):
    shop = db.query(Shops).filter(Shops.id == id).first()

    for params in data:
        shop.params = params

    try:
        db.add(shop)
        db.commit()
        db.refresh(shop)
    except Exception as error:
        print(error)

    return shop


def remove(id: int, db: Session):
    shop = db.query(Shops).filter(Shops.id == id).delete()
    db.commit()
    return shop