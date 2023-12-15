from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet

router = DefaultRouter()
router.register(r"category", CategoryViewSet, basename="category")
backend_urlpatterns = router.urls