from django.contrib import admin
from .models import ContactInfoModel, ContactModel

admin.site.register(ContactInfoModel)
admin.site.register(ContactModel)