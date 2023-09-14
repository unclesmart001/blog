from django.http import HttpResponse
from django.shortcuts import render


def login(request):
    return render(request, "authenticate/login.html")

def signup(request):
    return render(request, "authenticate/signup.html")

def login(request):
    return render(request, "authenticate/login.html")