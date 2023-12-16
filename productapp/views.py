from django.db import transaction

from rest_framework import viewsets
from rest_framework.exceptions import APIException

from productapp.models import Category, Product
from productapp.serializers import CategorySerializer, ProductSerializer
from rest_framework import generics


class CategoryViewSet(viewsets.ModelViewSet):

    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class ProductViewSet(viewsets.ModelViewSet):

    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class CategoryListAPIView(generics.ListAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        product_ids = self.request.query_params.getlist('product_ids', [])
        return Category.objects.filter(product__id__in=product_ids).distinct()
