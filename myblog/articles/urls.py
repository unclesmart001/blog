from django.urls import path
from  articles import views

app_name = "articles"
urlpatterns = [
    
    path("article/", views.article, name="article")
]
