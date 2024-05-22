from rest_framework.viewsets import ModelViewSet
from .models import ContactInfoModel, ContactModel
from rest_framework.decorators import api_view, permission_classes
from django.core.mail import send_mail
from rest_framework.response import Response
from .serializer import COntactInfoSerializer, ContactSerializer
from .permissions import IsSuperUser
from rest_framework import status
from rest_framework.permissions import AllowAny



@api_view(['POST', 'GET'])
@permission_classes([AllowAny])
def contact_view(request):
    try:
        if request.method == "POST":
            contact_user = ContactInfoModel.objects.all().last()
            first_name = request.data['first_name']
            email = request.data['email']
            message = request.data['message']


            send_mail(
                subject=f'New message from {first_name}',
                fail_silently=True,
                from_email=email,
                message=message,
                recipient_list=[contact_user.email, ]
            )

            ContactModel.objects.create(first_name=first_name, email=email, message=message)
            return Response({
                'message': 'Message successfully sended'
            }, status=status.HTTP_200_OK)

    except:
        return Response({
            'message': 'Something went wrong...'
        }, status=status.HTTP_400_BAD_REQUEST)


class ContactInfoViewSet(ModelViewSet):
    queryset = ContactInfoModel.objects.all()
    serializer_class = COntactInfoSerializer
    permission_classes = [IsSuperUser]

class ContactViewSet(ModelViewSet):
    queryset = ContactModel.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsSuperUser]