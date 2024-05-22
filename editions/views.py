from rest_framework.viewsets import ModelViewSet
from .models import EditionModel, EditionCategories
from .serializers import EditionSerializer, EditionCategorySerializer, EditionDetailSerializer
from .permissions import IsSuperUserOrReadOnly
from django_filters import rest_framework as filters
from rest_framework.pagination import PageNumberPagination


class EditionCatViewSet(ModelViewSet):
    queryset = EditionCategories.objects.all()
    serializer_class = EditionCategorySerializer
    permission_classes = [IsSuperUserOrReadOnly]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = '__all__'

class EditionViewSet(ModelViewSet):
    queryset = EditionModel.objects.all()
    serializer_class = EditionSerializer
    permission_classes = [IsSuperUserOrReadOnly]
    pagination_class = PageNumberPagination
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ('edition_name_uz', 'edition_name_en', 'edition_content_uz', 'edition_content_en', 'edition_categories', ) 

    def get_serializer_class(self):
        if self.request.method == "GET":
            return EditionDetailSerializer
        return EditionSerializer


