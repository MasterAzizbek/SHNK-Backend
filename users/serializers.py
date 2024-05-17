from rest_framework import serializers
from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user

    class Meta:
        model = CustomUser
        fields = ['first_name','last_name','birth_date','email','organization','login','password','degree','information','avatar']
