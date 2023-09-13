from typing import Type
from django.db import models
from django.contrib.auth.models import User
from django.db.models.options import Options
from writers.models import WriterProfile
from frontend.models import ReaderProfile

#creating a table in a database- a model is equavalent to a table i.e create table categoryx
class Category(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to="categories/images", null=True)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name

class Blog(models.Model):
    writer = models.ForeignKey(WriterProfile, on_delete=models.CASCADE, related_name= "blogs")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="blogs")
    published_on = models.DateTimeField()
    views = models.IntegerField()
    titles = models.CharField(max_length=30)
    content = models.TextField()
    #image = models.ImageField(upload_to="blog/images")
    is_approved = models.BooleanField(default=False)

class Comment(models.Model):
     blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="comments")
     sender = models.ForeignKey(ReaderProfile, on_delete=models.CASCADE, related_name="comments")
     message = models.TextField()
     created_at = models.DateTimeField(auto_now_add=True)

     def __str__(self):
         return f"{self.sender.user.username} : {self.blog.titles}"
     
     class Meta:
         ordering = ('-created_at',)

