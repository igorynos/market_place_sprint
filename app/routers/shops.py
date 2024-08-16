from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.dto import shops as ShopDTO
from app.services import shops as ShopService

router = APIRouter()


@router.get('/', tags=['shop'])
async def get_all(db: Session = Depends(get_db)):
    return ShopService.get_shops(db)


@router.post('/', tags=['shop'])
async def create(data: ShopDTO.Shops = None, db: Session = Depends(get_db)):
    return ShopService.create_shop(data, db)


@router.get('/{id}', tags=['shop'])
async def get(id: int = None, db: Session = Depends(get_db)):
    return ShopService.get_shop(id, db)


@router.put('/{id}', tags=['shop'])
async def update(id: int = None, data: ShopDTO.Shops = None, db: Session = Depends(get_db)):
    return ShopService.update(data, db, id)


@router.delete('/{id}', tags=['shop'])
async def delete(id: int = None, db: Session = Depends(get_db)):
    return ShopService.remove(id, db)
