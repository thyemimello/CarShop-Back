from django.db import models
from users.models import User
from django.contrib.auth import get_user_model

# Create your models here.
class Comment(models.Model):
    user_comment_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_id",null=True)
    comment = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_car_model():
        from advertisements.models import Car
        return Car

    car = models.ForeignKey('advertisements.Car', on_delete=models.CASCADE)
    
  