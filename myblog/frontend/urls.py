from django.urls import path
from  frontend import views

app_name = "frontend"
urlpatterns = [
    path("", views.home, name='home'),
    path("about/", views.about, name='about'),
    path("redirect_home/", views.redirect_home, name='redirect_home'),

]


