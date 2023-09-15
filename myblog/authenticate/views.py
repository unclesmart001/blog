from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login


def user_login(request):
    message=""
    if request.method =="POST":
        user = authenticate(
            username = request.POST.get("username"),
            password = request.POST.get("password"),
        )
        if user is not None:
            login(request, user)
            return redirect("frontend:home")
        else:
            message = "Invalid username and password"
    context = {
            "message": message
    }
    return render(request, "authenticate/login.html", context)

def signup(request):
    return render(request, "authenticate/signup.html")
