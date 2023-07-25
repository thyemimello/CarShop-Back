from rest_framework.serializers import ModelSerializer
from .models import Comment



class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "comment", "user_comment_id", "created_at", "advertisement"]
        read_only_fields = ["id", "user_comment_id", "created_at", "advertisement"]

        