from sqlalchemy.orm import Session

from app.dto import users
from app.models.users import Users


def get_users(db):
    return db.query(Users).all()


def create_user(data: users.Users, db):
    user = Users(first_name=data.first_name,
                 second_name=data.second_name,
                 email=data.email,
                 phone_number=data.phone_number,
                 )

    try:
        db.add(user)
        db.commit()
        db.refresh(user)
    except Exception as error:
        print(error)

    return user


def get_user(id: int, db):
    return db.query(Users).filter(Users.id == id).first()


def update(data: users.Users, db: Session, id: int):
    user = db.query(Users).filter(Users.id == id).first()

    for params in data:
        user.params = params

    try:
        db.add(user)
        db.commit()
        db.refresh(user)
    except Exception as error:
        print(error)

    return user


def remove(id: int, db: Session):
    user = db.query(Users).filter(Users.id == id).delete()
    db.commit()
    return user
