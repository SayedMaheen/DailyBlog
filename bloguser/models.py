
from django.contrib.auth.models import AbstractUser
from django.db import models


class BlogUser(models.Model):
    first_name= models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    username= models.CharField(max_length=255,unique=True)
    def __str__(self) -> str:
        return self.username

# use it by default anyway
class User(AbstractUser):
    email = models.EmailField(unique=True)

