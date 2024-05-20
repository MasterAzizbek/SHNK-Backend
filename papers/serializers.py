from rest_framework import serializers
from .models import PaperCategory, PapersModel, ReferencesModel, ReviewsModel



class PapersSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = PapersModel.objects.all()
        fields = ('author', 'paper_cat', 'paper_title_uz', 'paper_title_en', 'date', 'paper_content', 'keywords', 'article')
        

class PaperDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PapersModel
        fields = '__all__'

class PaperCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PaperCategory
        fields = '__all__'


class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewsModel
        fields = '__all__'


class ReferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReferencesModel
        fields = '__all__'