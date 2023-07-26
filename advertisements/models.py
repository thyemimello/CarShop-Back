from comments.models import Comment
from django.db import models
from users.models import User
# Create your models here.
class VehicleType (models.TextChoices):
    car = "car"
    motorcycles = "motorcycles"
    auctions = "auctions"


class Advertisements(models.Model):
    announcementType = models.CharField(max_length=255, default='SALE')
    title = models.TextField(max_length=255, null=True)
    year = models.IntegerField(null=True)
    km = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    description = models.TextField()
    vehicleType = models.CharField(choices=VehicleType.choices, default=VehicleType.auctions,max_length=255)
    published = models.BooleanField(default=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="car", null=True)

class Image(models.Model):
    vehicle = models.ForeignKey(Advertisements, related_name='images', on_delete=models.CASCADE)
    imageUrl = models.CharField(max_length=255)
    type = models.CharField(max_length=255)

   
   

