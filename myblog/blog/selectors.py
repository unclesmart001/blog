from blog.models import Category, Blog, Comment

#TODO Django model managers
'''
def add(*,x,y):
    return x+y

add(x=1,y=2)

example={
    "x" = 1
    "y" = 2
}

**example =(x=1, y=2)
add(**example)
'''


def get_categories(filter=None):
    '''
    Fetches all Blog category
    '''
    if not filter:
        categories = Category.objects.all()
        return categories
    
    if filter and isinstance(filter, dict):
       return Category.objects.filter(**filter)
    
    raise Exception("Filter must be a dictionary")

def get_specific_category(id:int) -> Category: 
    '''
    Returns an existing with the same ID
    '''
    category = Category.objects.get(pk=id)
    return category
     
def get_blog(filter = none):
  if not filter:
    return Blog.objects.all()
  
  if filter and isinstance(filter, dict):
    return Blog.objects.filter(**filter)
  raise Exception("Filter must be a dictionary")

def get_specific_blog(id:int):
    sp_blogs = Blog.objects.get(pk=id)
    return sp_blogs

 
def get_blog_comments(blog_id:int):
    comments = Comment.objects.filter(
        blog__id=blog_id
    )   
    return comments

def get_user_comments(user_id:int):
    sp_comments = Comment.objects.filter(
        sender__id=user_id
    )
    return sp_comments
