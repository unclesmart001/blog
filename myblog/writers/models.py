from django.db import models
from django.contrib.auth.models import User

class WriterProfile(models.Model):
    user = models.OneToOneField(User, models.CASCADE)
    education = models.TextField(null=True)
    about = models.TextField()
    cv = models.FileField(upload_to="writers/cv")
    profile_photo = models.ImageField(upload_to="writers/profile")

    def __str__(self) -> str:
        return self.user.username
    
    class Meta:
        ordering =("-id",)


  



