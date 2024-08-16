from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.dto import users as UserDTO
from app.services import users as UserService

router = APIRouter()


@router.get('/', tags=['user'])
async def get_all(db: Session = Depends(get_db)):
    return UserService.get_users(db)


@router.post('/', tags=['user'])
async def create(data: UserDTO.Users = None, db: Session = Depends(get_db)):
    return UserService.create_user(data, db)


@router.get('/{id}', tags=['user'])
async def get(id: int = None, db: Session = Depends(get_db)):
    return UserService.get_user(id, db)


@router.put('/{id}', tags=['user'])
async def update(id: int = None, data: UserDTO.Users = None, db: Session = Depends(get_db)):
    return UserService.update(data, db, id)


@router.delete('/{id}', tags=['user'])
async def delete(id: int = None, db: Session = Depends(get_db)):
    return UserService.remove(id, db)
