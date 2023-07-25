from comments.models import Comment
from django.db import models
from users.models import User
# Create your models here.

class Advertisements(models.Model):
    brand = models.CharField(max_length=60)
    model = models.CharField(max_length=120)
    year = models.IntegerField(null=True)
    fuel = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    quilometers = models.IntegerField(null=True)
    price = models.IntegerField(null=True)
    cover_img = models.CharField(max_length=150)
    description = models.TextField(max_length=250)
    is_avaliable = models.BooleanField(default=True)

    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="car", null=True)
   

