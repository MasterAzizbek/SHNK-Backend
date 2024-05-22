from .models import ContactInfoModel, ContactModel
from rest_framework import serializers



class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactModel
        fields = '__all__'

class COntactInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfoModel
        fields = '__all__'