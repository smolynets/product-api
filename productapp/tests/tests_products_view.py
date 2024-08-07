import pytest
import json
from django.urls import reverse

from productapp.models import Category, Product

pytestmark = pytest.mark.django_db


def test_product_list(auth_client):
    category = Category.objects.create(name="one")
    product = Product.objects.create(name="one", price=1)
    product.categories.add(category)
    response = auth_client.get(reverse("product-list"))
    assert response.json() == [
        {'id': product.id, 'name': 'one', 'price': '1.00', 'categories': [category.id]}
    ]
    response = auth_client.get(reverse("product-detail", args=[product.id]))
    assert response.json() == {
        'id': product.id, 'name': 'one', 'price': '1.00', 'categories': [category.id]
    }


def test_product_create(auth_client):
    assert Product.objects.count() == 0
    response = auth_client.post("/product/", data={"name": "test", "price": 1})
    new_product = Product.objects.get(name="test")
    assert response.status_code == 201
    assert response.json() == {'id': new_product.id, 'name': 'test', 'price': '1.00', 'categories': []}
    assert Product.objects.count() == 1


def test_product_update(auth_client):
    product = Product.objects.create(name="one", price=1)
    url = reverse("product-detail", args=[product.id])
    response = auth_client.put(
        url, data={"name": "test", "price": 2}, content_type="application/json"
    )
    assert response.status_code == 200
    assert response.json() == {'id': product.id, 'name': 'test', 'price': '2.00', 'categories': []}
    assert Product.objects.filter(name="test").filter(price=2).exists()


def test_product_partitial_update(auth_client):
    product = Product.objects.create(name="one", price=1)
    url = reverse("product-detail", args=[product.id])
    response = auth_client.patch(
        url, data={"name": "test"}, content_type="application/json"
    )
    assert response.status_code == 200
    assert response.json() == {'id': product.id, 'name': 'test', 'price': '1.00', 'categories': []}
    assert Product.objects.filter(name="test").exists()


def test_product_delete(auth_client):
    product = Product.objects.create(name="one", price=1)
    url = reverse("product-detail", args=[product.id])
    response = auth_client.delete(
        url, content_type="application/json"
    )
    assert response.status_code == 204
    assert Product.objects.count() == 0


def test_category_of_product_list(auth_client):
    category = Category.objects.create(name="one")
    product = Product.objects.create(name="one", price=1)
    # Use reverse to get the URL for the view
    url = reverse("category-of-product-list")
    # Append the query parameter to the URL
    url_with_params = f"{url}?product_ids={product.id}"
    response = auth_client.get(url_with_params)
    assert response.json() == []
    product.categories.add(category)
    response = auth_client.get(url_with_params)
    assert response.json() == [{'id': category.id, 'name': 'one', 'parent': None}]
    category_two = Category.objects.create(name="two")
    product.categories.add(category_two)
    response = auth_client.get(url_with_params)
    assert response.json() == [
        {'id': category.id, 'name': 'one', 'parent': None},
        {'id': category_two.id, 'name': 'two', 'parent': None}
    ]


def test_product_list_by_category_list(auth_client):
    category = Category.objects.create(name="one")
    product = Product.objects.create(name="one", price=1)
    response = auth_client.get(reverse("product_list_by_category_list", args=[category.id]))
    assert response.json() == []
    product.categories.add(category)
    response = auth_client.get(reverse("product_list_by_category_list", args=[category.id]))
    assert response.json() == [
        {'id': product.id, 'name': 'one', 'price': '1.00', 'categories': [category.id]}
    ]
