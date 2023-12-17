from django.db import transaction

from rest_framework import viewsets, generics, status
from rest_framework.exceptions import APIException

from productapp.models import Category, Product
from productapp.serializers import CategorySerializer, ProductSerializer, ParentCategorySerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class CategoryViewSet(viewsets.ModelViewSet):

    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class ProductViewSet(viewsets.ModelViewSet):

    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class CategoryListAPIView(generics.ListAPIView):
    """
    For a given list of products, retrieve all categories containing these products
    """
    serializer_class = CategorySerializer

    def get_queryset(self):
        product_ids = self.request.query_params.getlist('product_ids', [])
        return Category.objects.filter(product__id__in=product_ids).distinct()
    

class ProductListByCategoryView(generics.ListAPIView):
    """
    For a given category, retrieve a list of all products present in this category
    """
    serializer_class = ProductSerializer

    def get_queryset(self):
        category_id = self.kwargs.get('category_id')
        return Product.objects.filter(categories__id=category_id)
    

class CategoryDetailsView(generics.RetrieveAPIView):
    """
    For a given category, retrieve its descendant categories of all levels
    """
    queryset = Category.objects.all()
    serializer_class = ParentCategorySerializer

    def get_object(self):
        category_id = self.kwargs.get('category_id')
        return self.get_queryset().get(pk=category_id)
