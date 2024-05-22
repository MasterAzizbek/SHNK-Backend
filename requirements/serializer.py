from rest_framework import serializers
from .models import RequirementsModel


class RequirementSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequirementsModel
        fields = '__all__'

    
class RequirementsDetailSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(method_name='get_name', read_only=True)
    content = serializers.SerializerMethodField(method_name='get_content', read_only=True)

    class Meta:
        model = RequirementsModel
        fields = ['name', 'content']
    
    def get_name(self, obj):
        try:
            lang = self.context['request'].query_params.get('lang')

            if lang == 'en':
                return obj.requirement_title_en
            return obj.requirement_title_uz
        except:
            return obj.requirement_title_uz
        
    def get_content(self, obj):
        try:
            lang = self.context['request'].query_params.get('lang')

            if lang == 'en':
                return obj.requirement_content_en
            return obj.requirement_content_uz
        except:
            return obj.requirement_content_uz