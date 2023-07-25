from django.db import models
from users.models import User


# Create your models here.
class Comment(models.Model):
    user_comment_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_id",null=True)
    comment = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

    advertisement = models.ForeignKey('advertisements.Advertisements', on_delete=models.CASCADE, null=True)
    
  