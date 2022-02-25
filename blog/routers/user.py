from fastapi import APIRouter, Depends, status, HTTPException
from typing import List
from .. import schemas, models, database
from sqlalchemy.orm import Session
from ..repository import user


router= APIRouter(
    prefix='/user',
    tags=["Users"]
)
get_db= database.get_db

@router.post('/', response_model=schemas.ShowUser)
def create_user(request:schemas.User, db: Session= Depends(get_db)):
    return user.create(request, db)

@router.get('/{id}', response_model=schemas.ShowUser)
def get_use(id: int, db: Session= Depends(get_db)):
    return user.show(id, db)
