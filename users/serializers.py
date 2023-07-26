from django.core.validators import MinLengthValidator
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from address.models import Address
from address.serializers import AddressSerializer

from .models import User

class UserSerializer(serializers.ModelSerializer):
 
    class Meta:
        depth = 1
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
            "password": {"write_only": True,
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


    def create(self, validated_data: dict) -> User:
       address = validated_data.pop("address")
       user = User.objects.create_user(**validated_data)
       Address.objects.create(**address, user=user)
       return user
    


    def update(self, instance: User, validated_data: dict) -> User:
        for key, value in validated_data.items():
            if key == "password":
                instance.set_password(value)
          
            if key == "address":              
                for Key_address, value_address in value.items():
                  setattr(instance.address, Key_address, value_address)
                  instance.save()
            else:
                setattr(instance, key, value)
        instance.save()
        return instance
    
