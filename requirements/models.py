from django.db import models



class RequirementsModel(models.Model):
    requirement_title_uz = models.CharField(max_length=255)
    requirement_title_en = models.CharField(max_length=255)
    requirement_content_en = models.TextField()
    requirement_content_uz = models.TextField()