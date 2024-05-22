from rest_framework.routers import DefaultRouter
from .views import FaqViewSet


router = DefaultRouter()
router.register('', FaqViewSet)


urlpatterns = router.urls