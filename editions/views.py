from rest_framework.viewsets import ModelViewSet
from .models import EditionModel, EditionCategories
from .serializers import EditionSerializer, EditionCategorySerializer, EditionDetailSerializer
from .permissions import IsSuperUserOrReadOnly
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter, OrderingFilter


class EditionCatViewSet(ModelViewSet):
    queryset = EditionCategories.objects.all()
    serializer_class = EditionCategorySerializer
    permission_classes = [IsSuperUserOrReadOnly]

class EditionViewSet(ModelViewSet):
    queryset = EditionModel.objects.all()
    serializer_class = EditionSerializer
    permission_classes = [IsSuperUserOrReadOnly]
    filter_backends = [SearchFilter, OrderingFilter, ]
    search_fields = ['edition_content']

    def get_serializer_class(self):
        if self.request.method == "GET":
            return EditionDetailSerializer
        return EditionSerializer


class PublicationsView(ListAPIView):
    queryset = EditionModel.objects.filter(is_published=True)
    serializer_class = EditionSerializer
    permission_classes = [AllowAny]
    pagination_class = PageNumberPagination
    filter_backends = [SearchFilter, OrderingFilter, ]
    search_fields = ['edition_content']