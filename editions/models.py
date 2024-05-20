from django.db import models


class EditionCategories(models.Model):
    edition_cat_name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.edition_cat_name
    

class EditionModel(models.Model):
    edition_name_uz = models.CharField(max_length=255)
    edition_name_en = models.CharField(max_length=255)
    edition_photo = models.ImageField(upload_to='files/editions_images')
    edition_content_uz = models.TextField()
    edition_content_en = models.TextField()
    edition_categories = models.ManyToManyField(EditionCategories)
    edition_file_uz = models.FileField(upload_to='files/edition_files')
    edition_file_en = models.FileField(upload_to='files/edition_files')
    is_published = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.edition_name_uz