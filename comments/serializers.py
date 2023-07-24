from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

import advertisements
from .models import Comment



class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "comment", "user_id", "created_at"]
        read_only_fields = ["id", "user_id", "created_at"]

        advertisement_id = serializers.PrimaryKeyRelatedField(queryset=Comment.get_car_model().objects.all())