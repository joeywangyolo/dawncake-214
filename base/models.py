from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    
    avatar = models.ImageField(null=True, default="avatar.svg")
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username'] 

class Product(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True , null=True)
    price = models.DecimalField(max_digits=15 , decimal_places=2 , default=99.99)


