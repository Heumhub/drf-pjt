from django.db import models
from django.contrib.auth.models import AbstractUser


class Account(AbstractUser):
    user_name = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    nickname = models.CharField(max_length=30)
    birthday =  models.DateField()
    gender = models.CharField(max_length=5)
    introduction = models.TextField()





