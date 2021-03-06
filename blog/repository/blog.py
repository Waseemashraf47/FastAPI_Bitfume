from sqlalchemy.orm import Session
from ..import models, database, schemas
from fastapi import HTTPException, status

def get_all (db:Session):
    blogs=db.query(models.Blog).all()
    return blogs

def create (request: schemas.Blog, db: Session):
    new_blog= models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog
    #return db

def show (id: int, db:Session):
    blog=db.query (models.Blog).filter(models.Blog.id==id).first()

    if not blog:
        # response.status_code=status.HTTP_404_NOT_FOUND
        # return {'detail': f'The demanded Blog {id} is not available'}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                detail= (f'The demanded Blog {id} is not available'))  
    return blog

def destroy (id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                                detail=f"The Blog with {id} is not available")
    blog.delete(synchronize_session=False)
    db.commit()
    return 'Deleted'

def update (id: int, request: schemas.Blog, db:Session ):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                 detail=f"The Blog with {id} is not available")
    blog.update(request.dict())
    #blog.update(request)
    db.commit()
    #db.refresh()
    return 'UPDATED'