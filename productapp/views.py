from django.db import transaction

from rest_framework import viewsets, generics, status
from rest_framework.exceptions import APIException

from productapp.models import Category, Product
from productapp.serializers import (
    CategorySerializer, ProductSerializer, ParentCategorySerializer, CategoryOfferProductSerializer
)
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Count


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
    

class CategoryProductofferingCountAPIView(generics.ListAPIView):
    """
    For a given list of categories, retrieve the count of product offerings in each category
    """
    serializer_class = CategoryOfferProductSerializer

    def get_queryset(self):
        category_ids = self.request.query_params.getlist('category_ids', [])
        categories_query = Category.objects.filter(id__in=category_ids).distinct()
        res_with_num_products = categories_query.annotate(num_products=Count("product"))
        return res_with_num_products
