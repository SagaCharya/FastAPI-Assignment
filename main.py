from fastapi import FastAPI, HTTPException
from models.models import base_blog, create_blog, update_blog
from routes import routes




app = FastAPI(title='Blog App')

app.include_router(routes.router, prefix="", tags=["Blogs"])


     
