from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(max_length=60, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=150)
    cpf = models.CharField(max_length=11, unique=True)
    brithdate = models.DateField()
    profile_img = models.CharField(max_length=127)
    is_advertiser = models.BooleanField(default=False)   
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

   

    #   address_id = models.IntegerField(null=True, blank=True)

    