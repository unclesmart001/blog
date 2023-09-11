from django.urls import path
from  authenticate import views

app_name = "authenticate"
urlpatterns = [
    path("login/", views.login, name='login'),
    path("signup/", views.signup, name="signup")
]
