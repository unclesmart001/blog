from django.urls import path
from  staff import views

app_name = "staff"
urlpatterns = [
    path("home/", views.home, name='home'),
    path("login/", views.login, name='login'),
    path("writers/", views.writers, name="writers")
]
