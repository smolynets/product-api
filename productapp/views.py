from django.db import transaction

from rest_framework import viewsets
from rest_framework.exceptions import APIException

from productapp.models import Category, Product
from productapp.serializers import CategorySerializer, ProductSerializer


class CategoryViewSet(viewsets.ModelViewSet):

    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class ProductViewSet(viewsets.ModelViewSet):

    serializer_class = ProductSerializer
    queryset = Product.objects.all()
