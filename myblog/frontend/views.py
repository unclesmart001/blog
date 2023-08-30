
'''
Types of views
1. Class based views
2. Function based views

1. FUNCTION BASED VIEWS
-They take in one major parameter, request

def home(request):
#your code logic
#NB: you must return a response value
return response

HANDLING RESPONSES
1. Obtaining a http response in our browser

SyNTAX
    from django.http import HttpResponse

    def home(request):
    return HttpResponse("This is our home page")

#NB: Every view must have a url, which will be used to access be a client and make a request.

2. Obtaining a rendered HTML in our browser
 
SYNtax
from django.shortcuts import render

def home(request):
    return render(request, "path/to_template.html")
NB: We trace the path to a HTML document,from templates

EXAMPLE
def home(request):
    return render(request, "frontend/index.html")

TODO: 
In staff
1. create a view called writers for the page writers.html
2. Add a list of writers names(your own), which will be used as context
3. In your writers.html create a table containing the list of writes
    


'''
#from django.http import HttpResponse
from django.shortcuts import render, redirect


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

def redirect_home(request):
    print("-- Called redirect Home--")
    return redirect('staff:login')
