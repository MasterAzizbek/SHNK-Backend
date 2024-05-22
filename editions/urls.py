from .views import EditionCatViewSet, EditionViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('categories', EditionCatViewSet)
router.register('edition', EditionViewSet)


urlpatterns = router.urls