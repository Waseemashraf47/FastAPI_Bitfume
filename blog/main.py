from fastapi import FastAPI
from .import models
from .database import engine
from .routers import blog, user, authentication
#from passlib.context import CryptContext
# from .database import Base 
app=FastAPI()
models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)

# @app.post('/blog') #creating Blog

#get_db= database.get_db
#def get_db():
#    db = SessionLocal()
#    try:
#        yield db
#    finally:
#        db.close()
#creating Blog and Response Status
#@app.post('/blog',status_code=status.HTTP_201_CREATED, tags=["Blogs"])
#def create(request: schemas.Blog, db: Session= Depends(get_db)):
#    new_blog= models.Blog(title=request.title, body=request.body, user_id=1)
    #db.add(new_blog)
   # db.commit()
  #  db.refresh(new_blog)
 #   return new_blog
    #return db

#@app.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=["Blogs"])
#def destroy (id, db: Session=Depends(get_db)):
 #   blog = db.query(models.Blog).filter(models.Blog.id == id)
#    if not blog.first():
     #   raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
    #                            detail=f"The Blog with {id} is not available")
   # blog.delete(synchronize_session=False)

  #  db.commit()
    #db.refresh()
 #   return 'Deleted'


#@app.put('/blog/{id}', tags=["Blogs"])
#def update (id, request: schemas.Blog, db:Session=Depends(get_db)):
  #  blog = db.query(models.Blog).filter(models.Blog.id == id)
  #  if not blog.first():
    #    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
   #                              detail=f"The Blog with {id} is not available")
  #  blog.update(request.dict())
    #blog.update(request)
 #   db.commit()
   #db.refresh()
#    return 'UPDATED'


#@app.get('/blog', response_model=List[schemas.ShowBlog], tags=["Blogs"])
#def all(db: Session= Depends(get_db)):
#    blogs=db.query(models.Blog).all()
#    return blogs

#@app.get('/blog/{id}', status_code=200, response_model=schemas.ShowBlog, tags=["Blogs"])
#def show (id, response: Response, db: Session= Depends(get_db)):
#    blog=db.query (models.Blog).filter(models.Blog.id==id).first()

#    if not blog:
        # response.status_code=status.HTTP_404_NOT_FOUND
        # return {'detail': f'The demanded Blog {id} is not available'}
 #       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
  #              detail= (f'The demanded Blog {id} is not available'))  
   # return blog


#FOR PASSWORD ENCRYPTION
#pwd_cxt= CryptContext (schemes=["bcrypt"], deprecated="auto")
#CREATE USER
#@app.post('/user', response_model=schemas.ShowUser, tags=["Users"])
#def create_user(request:schemas.User, db: Session= Depends(get_db)):
    #hashedpassword=pwd_cxt.hash(request.password)
    #new_user=models.User(name=request.name, email=request.email, 
    #                        password=hashedpassword)
#    new_user=models.User(name=request.name, email=request.email, 
#                            password=Hash.bcrypt(request.password))
   # db.add(new_user)
   # db.commit()
  #  db.refresh(new_user)
 #   return new_user

#@app.get('/user/{id}', response_model=schemas.ShowUser, tags=["Users"])
#def get_user(id: int, db: Session= Depends(get_db)):
   # user=db.query(models.User).filter(models.User.id==id).first()
  #  if not user:
  #      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
 #               detail= (f'This user with id {id} is not available'))  
#    return user

