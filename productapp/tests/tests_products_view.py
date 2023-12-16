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
