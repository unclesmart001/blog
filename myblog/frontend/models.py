from typing import Type
from django.db import models
from django.contrib.auth.models import User
from django.db.models.options import Options

class ReaderProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #profile_image = models.ImageField(upload_to="/reader/photos", null=True)

    def __str__(self):
        return self.user.username
    
    class Meta:
        ordering = ("-id",)
