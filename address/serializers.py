from rest_framework import serializers
from .models import Address

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = [
            "id",
            "zip_code",
            "state",
            "city",
            "street",
            "number",
            "complement"         
        ]
        read_only_fields = ["id"]
