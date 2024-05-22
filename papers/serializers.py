from rest_framework import serializers
from .models import PaperCategory, PapersModel, ReviewsModel
from users.models import CustomUser
from django.db.models import Sum


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['login', 'degree', 'organization']

class PaperGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = PapersModel
        fields = ['id', 'paper_title_uz']
        

class ReviewsSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = ReviewsModel
        fields = '__all__'

class ReviewDetailSerializer(serializers.ModelSerializer):
    author = UserDetailSerializer()
    review_paper = PaperGetSerializer()

    class Meta:
        model = ReviewsModel
        fields = '__all__'
        depth = 1


class PapersSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = PapersModel
        fields = ('author', 'paper_cat', 'paper_title_uz', 'paper_title_en', 'date', 'paper_content_en', 'paper_content_uz' , 'keywords', 'article_en', 'article_uz', 'reference', )
        
class PaperDetailSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(method_name='get_name', read_only=True)
    content = serializers.SerializerMethodField(method_name='get_content', read_only=True)
    article = serializers.SerializerMethodField(method_name='get_article', read_only=True)
    reviews = serializers.SerializerMethodField(method_name='get_reviews', read_only=True)
    views_count = serializers.SerializerMethodField(method_name='get_views_count', read_only=True)

    class Meta:
        model = PapersModel
        fields = ('id','paper_cat', 'name', 'content', 'keywords', 'article', 'date', 'author', 'views_count', 'journal', 'reference', 'reviews',)

    def get_name(self, obj):
        lang = self.context['request'].query_params.get('lang', 'uz')  # Default to Uzbek if language is not specified
        return getattr(obj, f'paper_title_{lang}')

    def get_content(self, obj):
        lang = self.context['request'].query_params.get('lang', 'uz')
        return getattr(obj, f'paper_content_{lang}')

    def get_article(self, obj):
        lang = self.context['request'].query_params.get('lang', 'uz')
        return getattr(obj, f'article_{lang}')

    def get_reviews(self, obj):
        lang = self.context['request'].query_params.get('lang', 'uz')
        reviews_queryset = ReviewsModel.objects.filter(review_paper=obj.pk)
        serializer = ReviewDetailSerializer(reviews_queryset, many=True, context={'lang': lang})
        return serializer.data

    def get_views_count(self, obj):
        return obj.views_count.distinct().count()


class PaperCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PaperCategory
        fields = '__all__'

class CombinePaperToEdition(serializers.ModelSerializer):
    class Meta:
        model = PapersModel
        exclude = ['views_count']








