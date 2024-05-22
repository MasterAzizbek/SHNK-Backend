from .models import FaqModel
from rest_framework import serializers


class FaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = FaqModel
        fields = '__all__'

class FaqDetailSerializer(serializers.ModelSerializer):
    faq_title = serializers.SerializerMethodField(method_name='get_title', read_only=True)
    faq_content = serializers.SerializerMethodField(method_name='get_content', read_only=True)

    class Meta:
        model = FaqModel
        fields = ['faq_title', 'faq_content']


    def get_title(self, obj):
        try:
            lang = self.context['request'].query_params.get('lang')

            if lang == 'en':
                return obj.faq_title_en
            return obj.faq_title_uz
        except:
            return obj.faq_title_uz
    
    def get_content(self, obj):
        try:
            lang = self.context['request'].query_params.get('lang')

            if lang == 'en':
                return obj.faq_content_en
            return obj.faq_content_uz
        except:
            return obj.faq_content_uz