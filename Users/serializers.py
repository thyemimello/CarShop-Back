from django.core.validators import MinLengthValidator
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User

class UserSerializer(serializers.ModelSerializer):
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
           "adress_id",
           "created_at",
           "updated_at"
        ]
        read_only_fields = ["id", 
                            "is_advertiser", 
                            "adress_id", 
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
        return User.objects.create_user(**validated_data)

    def update(self, instance: User, validated_data: dict) -> User:
        for key, value in validated_data.items():
            if key == "password":
                instance.set_password(value)
            else:
                setattr(instance, key, value)
        instance.save()
        return instance