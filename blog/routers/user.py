from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from blog.db import get_db
from blog.repository.user import create_instance, get_instance
from blog.schemas import ShowUser, User

router = APIRouter(
    prefix='/user',
    tags=['users']
)


@router.post('/', response_model=ShowUser)
def create_user(request: User, db: Session = Depends(get_db)):
    return create_instance(request, db)


@router.get('/{id}', response_model=ShowUser)
def get_user(id: int, db: Session = Depends(get_db)):
    return get_instance(id, db)
