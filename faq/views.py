from .models import FaqModel
from .serializer import FaqDetailSerializer, FaqSerializer
from .permissions import IsSuperUser
from rest_framework.viewsets import ModelViewSet


class FaqViewSet(ModelViewSet):
    queryset = FaqModel.objects.all()
    serializer_class = FaqSerializer
    permission_classes = [IsSuperUser]


    def get_serializer_class(self):
        if self.request.method == 'GET':
            return FaqDetailSerializer
        return FaqSerializer