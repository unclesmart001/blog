from django.urls import path
from  authenticate import views

app_name = "authenticate"
urlpatterns = [
    path("login/", views.user_login, name='user_login'),
    path("signup/", views.signup, name="signup"),
]
