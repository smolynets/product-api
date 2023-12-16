from rest_framework.routers import DefaultRouter
from django.urls import path

from .views import CategoryViewSet, ProductViewSet, CategoryListAPIView, ProductListByCategoryView

router = DefaultRouter()
router.register(r"category", CategoryViewSet, basename="category")
router.register(r"product", ProductViewSet, basename="product")

urlpatterns = [
    path('category_of_product_list/', CategoryListAPIView.as_view(), name="category-of-product-list"),
    path(
        'product_list_by_category_list/<int:category_id>/',
        ProductListByCategoryView.as_view(),
        name="product_list_by_category_list"
    ),
]

urlpatterns += router.urls
