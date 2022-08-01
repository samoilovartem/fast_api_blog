from fastapi import FastAPI

from blog import models
from blog.db import engine
from blog.routers import authentication, user, blog

models.Base.metadata.create_all(bind=engine)


app = FastAPI()


app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)

