from rest_framework.routers import DefaultRouter

from .views import ApartmentViewSet

router = DefaultRouter()
router.register('apartments', ApartmentViewSet, basename='apartment')

urlpatterns = router.urls