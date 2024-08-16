from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.dto import products as ProductDTO
from app.services import products as ProductService

router = APIRouter()


@router.get('/', tags=['product'])
async def get_all(db: Session = Depends(get_db)):
    return ProductService.get_products(db)


@router.post('/', tags=['product'])
async def create(data: ProductDTO.Products = None, db: Session = Depends(get_db)):
    return ProductService.create_product(data, db)


@router.get('/{id}', tags=['product'])
async def get(id: int = None, db: Session = Depends(get_db)):
    return ProductService.get_product(id, db)


@router.put('/{id}', tags=['product'])
async def update(id: int = None, data: ProductDTO.Products = None, db: Session = Depends(get_db)):
    return ProductService.update(data, db, id)


@router.delete('/{id}', tags=['product'])
async def delete(id: int = None, db: Session = Depends(get_db)):
    return ProductService.remove(id, db)
