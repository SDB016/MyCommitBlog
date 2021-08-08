from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    github = models.CharField(max_length=100) 
    token = models.CharField(max_length=100)
    
