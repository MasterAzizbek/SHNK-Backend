from rest_framework.routers import DefaultRouter
from .views import PapersViewSet, ReviewVeiwSet, PaperCategoryViewSet,mainPageView
from django.urls import path

router = DefaultRouter()
router.register('papers', PapersViewSet)
router.register('category', PaperCategoryViewSet)
router.register('reviews', ReviewVeiwSet)

urlpatterns = [
    path('main/', mainPageView)
] + router.urls