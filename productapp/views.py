from django.db import transaction

from rest_framework import viewsets
from rest_framework.exceptions import APIException

from productapp.models import Category
from productapp.serializers import CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):

    serializer_class = CategorySerializer
    queryset = Category.objects.all()
