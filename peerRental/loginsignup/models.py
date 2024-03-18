from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=200)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']