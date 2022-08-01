from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from blog.db import get_db
from blog.repository.blog import show_all_instances, create_instance, delete_instance, update_instance, show_instance
from blog.schemas import ShowBlog, Blog, User

from blog.oauth2 import get_current_user

router = APIRouter(
    prefix='/blog',
    tags=['blogs']
)


@router.get('/', response_model=List[ShowBlog], status_code=status.HTTP_200_OK)
def show_all_blogs(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return show_all_instances(db)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_blog(request: Blog, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return create_instance(request, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return delete_instance(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_blog(id: int, request: Blog, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return update_instance(id, request, db)


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=ShowBlog)
def show_blog(id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return show_instance(id, db)

