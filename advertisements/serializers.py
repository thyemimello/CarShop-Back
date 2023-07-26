from rest_framework import serializers
from .models import Advertisements, Image

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'imageUrl', 'type']

class AdvertusementsSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)

    class Meta:
        model = Advertisements
        fields = ['id', 'announcementType', 'title', 'year', 'km', 'price', 'description', 'vehicleType', 'published', 'user_id', 'images']
