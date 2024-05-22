from rest_framework.viewsets import ModelViewSet
from .serializers import PaperCategorySerializer, PaperDetailSerializer, PapersSerializer, ReviewsSerializer, ReviewDetailSerializer, CombinePaperToEdition
from .permissions import IsAuthorOrReadOnly, IsSuperUser, IsReviewer
from .models import PapersModel, PaperCategory, ReviewsModel
from rest_framework.response import Response
from django_filters import rest_framework as filters
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from editions.serializers import EditionSerializer
from editions.models import EditionModel
from rest_framework.pagination import PageNumberPagination
from rest_framework import parsers


@api_view(['GET'])
@permission_classes([AllowAny])
def mainPageView(request):
    edition_serializer = EditionSerializer(EditionModel.objects.all().last(), context={'request': request})
    paper_serializer = PaperDetailSerializer(PapersModel.objects.all().order_by('-id')[:4], many=True, context={'request': request})
    most_read_paper_serializer = PaperDetailSerializer(PapersModel.objects.all().order_by('-views_count')[:4], many=True, context={'request': request})


    return Response(
        data={
            'LastEdition': edition_serializer.data,
            'LastPapers': paper_serializer.data,
            'MostReads': most_read_paper_serializer.data
        }
    )


class PapersViewSet(ModelViewSet):
    queryset = PapersModel.objects.all()
    serializer_class = PapersSerializer
    permission_classes = [IsAuthorOrReadOnly]
    pagination_class = PageNumberPagination
    filter_backends = [filters.DjangoFilterBackend]
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.FileUploadParser)
    filterset_fields = '__all__'

    
    def get_serializer_class(self):
        if self.request.method == "GET":
            return PaperDetailSerializer
        if self.request.method in ['PATCH', 'PUT']:
            if self.request.user.is_superuser:
                return CombinePaperToEdition
        return PapersSerializer
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if request.user.is_authenticated:
            if request.user not in instance.views_count.all():
                instance.views_count.add(request.user)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class PaperCategoryViewSet(ModelViewSet):
    queryset = PaperCategory.objects.all()
    serializer_class = PaperCategorySerializer
    permission_classes = [IsSuperUser]

class ReviewVeiwSet(ModelViewSet):
    queryset = ReviewsModel.objects.all()
    serializer_class = ReviewsSerializer
    permission_classes = [IsReviewer]

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ReviewDetailSerializer
        return ReviewsSerializer

