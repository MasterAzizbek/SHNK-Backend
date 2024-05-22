from django.db import models
from django.contrib.auth import get_user_model

class PaperCategory(models.Model):
    cat_name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.cat_name

class PapersModel(models.Model):
    paper_cat = models.ManyToManyField(PaperCategory)
    paper_title_uz = models.CharField(max_length=300)
    paper_title_en = models.CharField(max_length=300)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    views_count = models.ManyToManyField(get_user_model(), related_name='views', blank=True)
    paper_content_uz = models.TextField()
    paper_content_en = models.TextField()
    keywords = models.CharField(max_length=500)  
    article_uz = models.TextField()
    article_en = models.TextField()
    journal = models.ForeignKey('editions.EditionModel', on_delete=models.CASCADE, null=True, blank=True)
    reference = models.TextField()
    reviews = models.ManyToManyField('ReviewsModel', null=True, blank=True)
    
    def __str__(self) -> str:
        return self.paper_title_uz


class ReviewsModel(models.Model):
    author = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    review_file = models.FileField(upload_to='files/review_files')
    review_paper = models.ForeignKey(PapersModel, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.author)
