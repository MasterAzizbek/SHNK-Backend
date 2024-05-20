from .views import EditionCatViewSet, EditionViewSet, PublicationsView
from rest_framework.routers import DefaultRouter
from django.urls import path

router = DefaultRouter()
router.register('categories', EditionCatViewSet)
router.register('edition', EditionViewSet)


urlpatterns = [
    path('publications/', PublicationsView.as_view())
] + router.urls