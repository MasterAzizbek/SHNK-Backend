from .views import RequirementsViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('', RequirementsViewSet)

urlpatterns = router.urls