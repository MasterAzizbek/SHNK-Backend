from rest_framework.generics import CreateAPIView
from .serializers import UserSerializer
from .models import CustomUser, PasswordResets
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.core.mail import send_mail
from random import randint
from rest_framework import parsers

class RegisterView(CreateAPIView):
    queryset = CustomUser.objects.all() 
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.FileUploadParser)

    def perform_create(self, serializer):
        serializer.save()


@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def passwordChangeView(request):
    if request.method == 'POST':
        try:
            email = request.data['email']
            user = CustomUser.objects.get(email=email)
        except KeyError:
            return Response({"message": "Email is required in the request"}, status=status.HTTP_400_BAD_REQUEST)
        except CustomUser.DoesNotExist:
            return Response({"message": "User with this email does not exist"}, status=status.HTTP_404_NOT_FOUND)
        
        old_password = request.data.get('old_password')
        new_password = request.data.get('new_password')

        if user.check_password(old_password):
            user.set_password(new_password)
            user.save()
            return Response(
                {
                    "message": "Password changed successfully"
                },
                status=status.HTTP_200_OK
            )
        else:
            return Response({"message": "Old password is incorrect"}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({"message": "Unsupported method"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    

@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def password_reset(request):
    if request.method == 'POST':
        try:
            email = request.data['email']
            user = CustomUser.objects.get(email=email)
        except KeyError:
            return Response({"message": "Email is required in the request"}, status=status.HTTP_400_BAD_REQUEST)
        except CustomUser.DoesNotExist:
            return Response({"message": "User with this email does not exist"}, status=status.HTTP_404_NOT_FOUND)

        code = ''.join([str(randint(0, 9)) for _ in range(4)])

        send_mail(
            subject="Password reset code",
            from_email='masternajottalim@gmail.com',
            fail_silently=True,
            message=f"Hello dear customer. Your code {code}",
            recipient_list=[email,]
        )

        PasswordResets.objects.create(email=email, code=code)
        return Response({"message": "Password reset code sent successfully"}, status=status.HTTP_200_OK)
    else:
        return Response(
            {
                'message': "Unsupported method"
            },
            status=status.HTTP_405_METHOD_NOT_ALLOWED
        )

@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def password_reset_confirm(request):
    if request.method == 'POST':
        try:
            email = request.data['email']
            code = request.data['code']
            new_password = request.data['new_password']
            password_confirm = request.data['confirm_password']
            user = CustomUser.objects.get(email=email)
            user_code_emails = PasswordResets.objects.filter(email=email)

            if user_code_emails.count() == 0:
                return Response(
                    {"message": "No password reset code found for this email"},
                    status=status.HTTP_400_BAD_REQUEST
                )

            for user_code_email in user_code_emails:
                if user_code_email.code == code:
                    if new_password == password_confirm:
                        user.set_password(new_password)
                        user.save()
                        user_code_emails.delete() 
                        return Response(
                            {"message": "Password reset successfully"},
                            status=status.HTTP_200_OK
                        )
                    else:
                        return Response(
                            {"message": "Passwords didn't match!"},
                            status=status.HTTP_400_BAD_REQUEST
                        )
            return Response(
                {"message": "Confirmation code is incorrect!"},
                status=status.HTTP_400_BAD_REQUEST
            )
        except CustomUser.DoesNotExist:
            return Response(
                {"message": "User with this email does not exist"},
                status=status.HTTP_404_NOT_FOUND
            )
    else:
        return Response(
            {'message': "Unsupported method"},
            status=status.HTTP_405_METHOD_NOT_ALLOWED
        )
    
