from django.core.validators import MinLengthValidator
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from address.models import Address
from address.serializers import AddressSerializer
from django.db import transaction

from .models import User

class UserSerializer(serializers.ModelSerializer):
    address = AddressSerializer(many=False)
    class Meta:
        model = User 
        fields = [
            "id",
            "username",
            "email",
            "password",
            "cpf",
            "brithdate",
           "profile_img",
           "is_advertiser",       
           "created_at",
           "updated_at",
           "address"
        ]
        read_only_fields = ["id", 
                            "is_advertiser", 
                            "created_at",
                            "updated_at"
                            ]
        extra_kwargs = {
            "password": {
                         "validators":[MinLengthValidator(8)]},
            "username": {
                "validators": [
                    UniqueValidator(
                        queryset=User.objects.all(),
                        message="A user with that username already exists.",
                    ),
                ],
            },
             "email": {
                "validators": [
                    UniqueValidator(
                        queryset=User.objects.all(),
                        message="This field must be unique.",
                    ),
                ],
            },
        }

    def create(self, validated_data):
        address_data = validated_data.pop('address')
        with transaction.atomic():
            user = User.objects.create_user(**validated_data)
            Address.objects.create(user=user, **address_data)
        return user

    def update(self, instance, validated_data):
        address_data = validated_data.pop('address', None)
        for key, value in validated_data.items():
            if key == "password":
                instance.set_password(value)
            else:
                setattr(instance, key, value)
        instance.save()

        if address_data:
            address = instance.address
            if address:
                for key, value in address_data.items():
                    setattr(address, key, value)
                address.save()

        return instance