from django.db import models
from users.models import User


class Address(models.Model):
           
    zip_code = models.CharField(max_length=8, unique=True)
    state = models.CharField(max_length=2)
    city = models.CharField(max_length=25)
    street = models.CharField(max_length=40, unique=True)
    number = models.CharField(max_length=4, unique=True)
    complement = models.CharField(max_length=128, null=True, blank=True)

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='address', null=True, blank=True)


  
    
