'''
TODO: 
In staff
1. create a view called writers for the page writers.html
2. Add a list of writers names(your own), which will be used as context
3. In your writers.html create a table containing the list of writers
    



from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    username = "Chege"
    paragraph = "My first Django paragraph"

    names_list = [
        'mango','orange', 'pink', 'green', 'violet'
    ]
    context = {
        'name' : username,
        'paragraph' : paragraph,
        'names_list' : names_list
    }
    return render(request, "frontend/index.html", context)

def about(request):
    return render(request, "frontend/about.html")
'''

from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse("This is our staff home page")

def login(request):
    return HttpResponse('Login to view-staff')

def writers(request):
    writers_list = [
        {   'id' : 1,
            'author' : 'Chinua Achebbe', 
             'title' : "Things fall apart"},

        {   ' id' : 2,
            'author' : 'Paulo Cuelho' ,
            ' title' : "The Alchemist"},

        {'id': 3,
         'author': 'Robin Sharma',
         ' title': "The Monk who Sold his Ferrari"},
        
    ]

    context = {
        "writers" : writers_list
    }

    return render(request, 'staff/writers.html', context)










