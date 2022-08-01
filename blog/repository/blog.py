from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from blog import models
from blog.schemas import Blog


def show_all_instances(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs


def create_instance(request: Blog, db: Session):
    new_blog = models.Blog(
        title=request.title,
        body=request.body,
        user_id=1,
    )
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def delete_instance(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Unfortunately, there is no blog with id {id}')
    blog.delete(synchronize_session=False)
    db.commit()
    return {'detail': f'The blog with id {id} has been deleted'}


def update_instance(id: int, request: Blog, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Unfortunately, there is no blog with id {id}')
    blog.update(request.dict())
    db.commit()
    return {'detail': f'The blog with id {id} has been updated'}


def show_instance(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Unfortunately, there is no blog with id {id}')
    return blog
