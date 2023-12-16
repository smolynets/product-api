import pytest
import json
from django.urls import reverse

from productapp.models import Category, Product

pytestmark = pytest.mark.django_db


def test_product_list(client):
    category = Category.objects.create(name="one")
    product = Product.objects.create(name="one", price=1)
    product.categories.add(category)
    response = client.get(reverse("product-list"))
    assert response.json() == [{'id': 1, 'name': 'one', 'price': '1.00', 'categories': [1]}]
    response = client.get(reverse("product-detail", args=[product.id]))
    assert response.json() == {'id': 1, 'name': 'one', 'price': '1.00', 'categories': [1]}


def test_product_create(client):
    assert Product.objects.count() == 0
    response = client.post("/product/", data={"name": "test", "price": 1})
    assert response.status_code == 201
    assert response.json() == {'id': 1, 'name': 'test', 'price': '1.00', 'categories': []}
    assert Product.objects.count() == 1


def test_product_update(client):
    product = Product.objects.create(name="one", price=1)
    url = reverse("product-detail", args=[product.id])
    response = client.put(
        url, data={"name": "test", "price": 2}, content_type="application/json"
    )
    assert response.status_code == 200
    assert response.json() == {'id': 1, 'name': 'test', 'price': '2.00', 'categories': []}
    assert Product.objects.filter(name="test").filter(price=2).exists()


def test_product_partitial_update(client):
    product = Product.objects.create(name="one", price=1)
    url = reverse("product-detail", args=[product.id])
    response = client.patch(
        url, data={"name": "test"}, content_type="application/json"
    )
    assert response.status_code == 200
    assert response.json() == {'id': 1, 'name': 'test', 'price': '1.00', 'categories': []}
    assert Product.objects.filter(name="test").exists()


def test_product_delete(client):
    product = Product.objects.create(name="one", price=1)
    url = reverse("product-detail", args=[product.id])
    response = client.delete(
        url, content_type="application/json"
    )
    assert response.status_code == 204
    assert Product.objects.count() == 0


def test_category_of_product_list(client):
    category = Category.objects.create(name="one")
    product = Product.objects.create(name="one", price=1)
    # Use reverse to get the URL for the view
    url = reverse("category-of-product-list")
    # Append the query parameter to the URL
    url_with_params = f"{url}?product_ids={product.id}"
    response = client.get(url_with_params)
    assert response.json() == []
    product.categories.add(category)
    response = client.get(url_with_params)
    assert response.json() == [{'id': 1, 'name': 'one', 'parent': None}]
    category_two = Category.objects.create(name="two")
    product.categories.add(category_two)
    response = client.get(url_with_params)
    assert response.json() == [
        {'id': 1, 'name': 'one', 'parent': None}, {'id': 2, 'name': 'two', 'parent': None}
    ]


def test_product_list_by_category_list(client):
    category = Category.objects.create(name="one")
    product = Product.objects.create(name="one", price=1)
    response = client.get(reverse("product_list_by_category_list", args=[category.id]))
    assert response.json() == []
    product.categories.add(category)
    response = client.get(reverse("product_list_by_category_list", args=[category.id]))
    assert response.json() == [{'id': 1, 'name': 'one', 'price': '1.00', 'categories': [1]}]
