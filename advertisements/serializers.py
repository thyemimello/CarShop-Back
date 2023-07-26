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
        fields = [ 'id','announcementType', 'title', 'year', 'km', 'price', 'description', 'vehicleType', 'published', 'user_id', 'images']

    def create(self, validated_data):
        images_data = validated_data.pop('images')
        advertisement = Advertisements.objects.create(**validated_data)
        for image_data in images_data:
            Image.objects.create(vehicle=advertisement, **image_data)
        return advertisement