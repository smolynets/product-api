from rest_framework import serializers

from productapp.models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name", "parent")


class ParentCategorySerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ("id", "name", "children")

    def get_children(self, instance):
        children = Category.objects.filter(parent__id=instance.id)
        serializer = ParentCategorySerializer(children, many=True)
        return serializer.data


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "name", "price", "categories")


class CategoryOfferProductSerializer(serializers.ModelSerializer):
    num_products = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ("id", "name", "num_products")

    def get_num_products(self, instance):
        return instance.num_products
