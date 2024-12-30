
from pydantic import BaseModel, Field


class base_blog(BaseModel):
    title: str = Field(description='Title of the blog')
    content: str = Field(description='Main Content of the blog')
    author: str = Field(description='Author of the bolg')

class create_blog(base_blog):
    pass

class update_blog(base_blog):
    content: str | None
    author: str | None





