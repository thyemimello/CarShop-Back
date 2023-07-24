from rest_framework.serializers import ModelSerializer
from .models import Car

class AdvertusementsSerializer(ModelSerializer):
   class Meta:
      model = Car
      fields = [
         "brand",
         "model",
         "year",
         "fuel",
         "color",
         "quilometers",
         "price",
         "cover_img",
         "description",
         "is_avaliable",
         "user_id"
      ]
      read_only_fields = ["id", "user_id"]

      