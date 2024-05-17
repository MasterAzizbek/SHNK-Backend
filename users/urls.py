from django.urls import path
from .views import RegisterView, passwordChangeView, password_reset, password_reset_confirm


urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('password_change/', passwordChangeView),
    path('password_reset/', password_reset),
    path('password_reset_confirm/', password_reset_confirm)
]