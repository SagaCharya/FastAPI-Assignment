from fastapi import APIRouter, HTTPException
from models.models import base_blog, create_blog, update_blog
from db.db import db_base

router = APIRouter()

@router.get(
        '/',
        summary="Retrieve all blogs",
        description="Fetch all blog posts in the system.", 
        response_model=list[base_blog])
async def get_blogs() -> list[base_blog]:
    return db_base

@router.post('/create',
            summary="Create a new blog",
            description="Creates the blog in the in-Memory Database", 
            response_model= base_blog,
            responses={
                400:{'description': 'Blog with given name already exists'}
            })
async def create_blog(blog_data : create_blog) -> base_blog:
    for blog in db_base:
        if blog["title"] == blog_data.title:
            raise HTTPException(status_code=400, detail='Blog with this name already exist')
    db_base.append(blog_data.dict())
    return blog_data

@router.put("/update/{title}",
            summary="Update a blog",
            description="Updates the blog by blog's 'Title'",
            response_model= base_blog, 
            responses = {
                404: {'discription': 'Blog with given title not found'}
            })
async def update_blog(title:str, blog_data: update_blog):
    for blog in db_base:
        if blog['title'] == title:
            if blog_data.content is not None:
                blog['content'] = blog_data.content 
            if blog_data.author is not None:
                blog['author'] = blog_data.author 
            return blog 
    raise HTTPException(status_code=404, detail='Blog not found')

@router.delete('/delete/{title}',
               summary="Delete a blog", 
               description="Delete a blog by blog's 'Title'",
               responses={
                   404: {'description': 'Blog with given title not found'},
                   200: {'description': 'Blog deleted Successfully'},
               })
async def delete_blog(title:str):
    for blog in db_base:
        if blog['title'] == title:
            db_base.remove(blog)
            return{'details':f"Blog '{title}' deleted!'"}
    raise HTTPException(status_code=404, detail='Blog not found')
        
