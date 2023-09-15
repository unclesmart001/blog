'''
DJANGO COMMANDS
-Django system have a file structure composed of:
1. The Project: This is the project directory that holds the whole project.
2. Configurations directory: Usually named the same as the project directory.it is created together with the project , it contains configutions that govern the execution of the entire project.
3. manage.py: This is a python file, that is responsible for all operational commands within our project i.e Creating new apps, making migrations, creating admin users etc.ls


4.Apps: Django structures sections of the project into packages(folders with __init__.py) commonly reffered to as "app" in django specifically.

CREATING A NEW DJANGO PROJECT

cmd: django-admin startproject 'ProjectName'
Eg: django-admin startproject 'Blog'

NB: This works after you have activated your envt.

source "PATH TO ACTIVATE: E.G. blogenv/Scripts/activate

#TODO: 
1. Create .env, a variable DJANGO_SECRET_KEY, load the secret key variable from  settings.py, dont forget to install dotenv in your evnt
2. what is WSGI? why does it matter?
3. what is ASGI? why does it matter?


1. Create a new module named writers
2. go read on views.py in django

1. Create "about" view inside frontend app
2. Add its url path in mblog.urls
3 create login view inside writers app
4 Add its url path inside myblog.urls 


1. Create the app 'staff'
2. Create the view 'home' and 'login' in staff views
3. Create thier respectives urls as demonstrated previously in frontend and writers


MODEL VIEW TEMPLATE(MVT)
1. VIEW LAYER
-Deals with handling requests and responses in our system, it is also directly involved in handling the system logics: e.g login/signup logic



'''
