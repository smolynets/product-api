from rest_framework.routers import DefaultRouter
from django.urls import path

from .views import (
    CategoryViewSet,
    ProductViewSet,
    CategoryListAPIView,
    ProductListByCategoryView,
    CategoryDetailsView,
    CategoryProductofferingCountAPIView,
    CategoryProductTotalofferingCountAPIView
)

router = DefaultRouter()
router.register(r"category", CategoryViewSet, basename="category")
router.register(r"product", ProductViewSet, basename="product")

urlpatterns = [
    path('category-of-product-list/', CategoryListAPIView.as_view(), name="category-of-product-list"),
    path(
        'product-by-category-list/<int:category_id>/',
        ProductListByCategoryView.as_view(),
        name="product_list_by_category_list"
    ),
    path(
        'category-parents-list/<int:category_id>/',
        CategoryDetailsView.as_view(),
        name="category_parents_list"
    ),
    path(
        'category-product-offering-count-apiview/',
        CategoryProductofferingCountAPIView.as_view(),
        name="category-product-offering-count-apiview"
    ),
    path(
        'category-product-total-offering-count-apiview/',
        CategoryProductTotalofferingCountAPIView.as_view(),
        name="category-product-total-offering-count-apiview"
    ),
]

urlpatterns += router.urls
