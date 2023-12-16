from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet, ProductViewSet

router = DefaultRouter()
router.register(r"category", CategoryViewSet, basename="category")
router.register(r"product", ProductViewSet, basename="product")
backend_urlpatterns = router.urls