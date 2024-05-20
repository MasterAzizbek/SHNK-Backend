from rest_framework import serializers
from django.contrib.sites.shortcuts import get_current_site
from .models import EditionModel, EditionCategories


class EditionCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = EditionCategories
        fields = '__all__'


class EditionDetailSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(method_name='get_name', read_only=True)
    content = serializers.SerializerMethodField(method_name='get_content', read_only=True)
    file = serializers.SerializerMethodField(method_name='get_file', read_only=True)
    

    class Meta:
        model = EditionModel
        fields = ('name', 'content', 'file', 'edition_photo', 'edition_categories', )
        depth = 1

    def get_name(self, obj):
        try:
            lang = self.context['request'].query_params.get('lang')
            if lang == 'en':
                return obj.edition_name_en
            return obj.edition_name_uz
        except:
            return obj.edition_name_uz
        
    def get_content(self, obj):
        try:
            lang = self.context['request'].query_params.get('lang')
            if lang == 'en':
                return obj.edition_content_en
            return obj.edition_content_uz
        except:
            return obj.edition_content_uz          

    def get_file(self, obj):
        request = self.context.get('request')
        domain_name = get_current_site(request).domain
        try:
            lang = self.context['request'].query_params.get('lang')
            if lang == 'en':
                return f"https://{domain_name}{obj.edition_file_en.url}"
            return f"https://{domain_name}{obj.edition_file_uz.url}"
        except:
            return f"https://{domain_name}{obj.edition_file_uz.url}" 

        
class EditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = EditionModel
        fields = '__all__'