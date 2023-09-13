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
        Category.objects.filter(**filter)

def get_specific_category(id:int) -> Category: 
    '''
    Returns an existing with the same ID
    '''
    category = Category.objects.get(pk=id)
    return category
     
def get_blog():
    all_blogs = Blog.objects.all()
    return all_blogs

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
    
'''
creating Read queries in django
-we use queries to obtain data from our database. This data can be in form of a QuerySet or a QueryDict.

A queryset is a list of data items retrieved from our database, under a particular model.
A querydict is a specific object retrieved from our database under  a particular model.

How to get a QueryDict(a model object)
Syntax: Model.objects.get(unique_field=unique_value)

-With the .get() we are able to retrieve a single  instance from a model; However if more than value is found ,this raises an error. also if the field value does not exist fo any instance in our model we will get an ObjectDoesNotExist exception.
Example: Blog.objects.get(id=1)

How to get QuerySet
We get a queryset either when retrieving all data or specific data.

Retrieving all data
Syntax: Model.objects.all()
E.G Blog.objects.all()

Retrieving data by filtering 
Syntax: Model.objects.filter(field1=value1, field2=value2)
EG: Blog.objects.filter(title="sth")

Advanced filtering
1. lesser than(__lt), greater than(__gt), greater or equal to(__gte), less or equal to(__lte)
-Their main use case is in:
  a. Getting a duration eg between the beginning of the month to today in a system. e.g getting Blogs written in btw a specific timeframe
  b. Getting an age bracket in a system: e.g getting movies for teens or adult in a site like netflix
  c. Gettting a price range e.g in an ecommerce system

  They therefore work with date fields or number fields(float/decimals/int/double)
  How to use them in Django:
  Syntax: Model.objects.filter(field__lte=value)
  Example: Filtering Blogs written btw start of this sept and yesterday

  Import datetime
  yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
  start_of_sep = datetime.now().replace(day=1, month=8)

  blogs = Blog.objects.filter(
                 created_at__lte=yesterday,
                created_at__gte=start_of_sep
            )

2. String contains (__icontains), string is exactly (__iexact), String starts with (__startwith), String ends with (__endswith)

- This is used on string fields. We mainly use it for search, in a particular fields. I.e: We can check for a blog whose title starts with a particular set of character.

blogs = Blog.objects.filter(title__startswith="sth")

>> __icontains: Checks if the string contains the privided string.
>> __iexact: Checks if the string is exactly equal to the privided string.
>> __iendswith: Checks if the string ends with the provided string.

-Mainly used in searches in different types of websites e.g Blog search, Movie search, Product search

3. Items in queyset/list(__in): The input of this is a list or a queryset. It is used to check if a field value is in a list.
E.g User.objects.filter(role__in=[RoleType.ADMIN, RoleType.SUPERUSER])
The query above is used to check if a use's role is either an adin or a superuser(NB: There is an abstraction of the Roletype code), then we can use this info to determine the logic that comes afterwards

use cases
>>The one illustrated above
TODO: look at other usecases

4. Working with foreign fields (TODO: look at how to work with foreign fields in Django )

'''
















'''
Elitebook@DESKTOP-PFSQFAA MINGW32 ~/OneDrive/Desktop/Django course/BackEnd/learning_django
$ source blogenv/Scripts/activate
(blogenv) 
Elitebook@DESKTOP-PFSQFAA MINGW32 ~/OneDrive/Desktop/Django course/BackEnd/learning_django
$ pip install pillow
Collecting pillow
  Using cached Pillow-10.0.0.tar.gz (50.5 MB)
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Building wheels for collected packages: pillow
  Building wheel for pillow (pyproject.toml) ... error
  error: subprocess-exited-with-error
  
  × Building wheel for pillow (pyproject.toml) did not run successfully.
  │ exit code: 1
  ╰─> [205 lines of output]
'''

'''
     writing manifest file 'src\Pillow.egg-info\SOURCES.txt'
      running build_ext
     
     
      The headers or library files could not be found for zlib,
      a required dependency when compiling Pillow from source.
     
      Please see the install instructions at:
         https://pillow.readthedocs.io/en/latest/installation.html

'''
