from django.db import models

class FaqModel(models.Model):
    faq_title_en = models.CharField(max_length=500)
    faq_title_uz = models.CharField(max_length=500)
    faq_content_en = models.TextField()
    faq_content_uz = models.TextField()


    def __str__(self) -> str:
        return self.faq_title_en