from rest_framework.viewsets import ModelViewSet
from .models import RequirementsModel
from .serializer import RequirementSerializer,RequirementsDetailSerializer
from .permissions import IsSuperUser


class RequirementsViewSet(ModelViewSet):
    queryset = RequirementsModel.objects.all()
    serializer_class = RequirementSerializer
    permission_classes = [IsSuperUser]


    def get_serializer_class(self):
        if self.request.method == 'GET':
            return RequirementsDetailSerializer
        return RequirementSerializer