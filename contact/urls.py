from rest_framework.routers import DefaultRouter
from .views import contact_view, ContactInfoViewSet, ContactViewSet
from django.urls import path

router = DefaultRouter()
router.register('contact', ContactViewSet)
router.register('info', ContactInfoViewSet)


urlpatterns = [
    path('send/', contact_view)
] + router.urls