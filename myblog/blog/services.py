from . import selectors
from blog.models import Category, Blog, Comment
from writers.models import WriterProfile



"""
Database changes operations i.e: create, Update, Delete / manipulating the table in the database
"""
def create_category(input_name:str, input_description:str):
    try:
        category= Category.objects.create(
            name = input_name,
            description = input_description
        )
        return category
    except Exception as e:
        raise str(e)

def create_blog(
        writer: WriterProfile,
        category: Category,
        published_on ,
        title ,
        content: str,
        is_approved: bool, 
)->Blog:
    try:
        blog = Blog.objects.create(
            writer = writer,
            category = category,
            published_on = published_on,
            title= title,
            content = content,
            is_approved = is_approved
        )
        return blog
    except Exception as e:
        raise str(e)
    
def update_category(category_id: int,updates: dict)-> Category:
    try:
        category_instance = selectors.get_specific_category(category_id)
        if isinstance(updates, dict):
            return category_instance.update(**updates)
        raise Exception("Please provide a dictionary")
    except Exception as e:
        raise str(e)

def update_blog(blog_id: int, update: dict)->Blog:
    try:
        blog_instance = selectors.get_specific_blog(blog_id)
        if isinstance(update, dict):
            return blog_instance.update(**update)
        raise Exception("please provide a dictionary")
    except Exception as e:
        raise str(e)

def delete_category(categories_id: int):
    category_instance = selectors.get_specific_category(categories_id)
    category_instance.delete()

def delete_blog(blog_id: int):
    blog_instance = selectors.get_specific_blog(blog_id)
    blog_instance.delete()

    '''
    TODO
    1. create an enviroment
    2. django model forms
    
    '''
