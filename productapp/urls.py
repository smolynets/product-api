from rest_framework.routers import DefaultRouter
from django.urls import path

from .views import CategoryViewSet, ProductViewSet, CategoryListAPIView

router = DefaultRouter()
router.register(r"category", CategoryViewSet, basename="category")
router.register(r"product", ProductViewSet, basename="product")

# urlpatterns += router.urls
urlpatterns = [
    path('category_of_product_list/', CategoryListAPIView.as_view(), name="category-of-product-list"),
]

urlpatterns += router.urls
