from django.urls import path
from writers import views

app_name = "writers"
urlpatterns =[
    path("login/", views.login, name="login")
    
]

