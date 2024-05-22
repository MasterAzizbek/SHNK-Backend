from django.db import models


class ContactModel(models.Model):
    first_name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()


    def __str__(self) -> str:
        return self.first_name
    
class ContactInfoModel(models.Model):
    adress = models.CharField(max_length=500)
    phone_number = models.CharField(max_length=255)
    email = models.EmailField()