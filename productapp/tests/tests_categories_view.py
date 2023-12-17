import pytest
import json
from django.urls import reverse

from productapp.models import Category, Product

pytestmark = pytest.mark.django_db


def test_category_list(client):
    category = Category.objects.create(name="one")
    response = client.get(reverse("category-list"))
    assert response.json() == [{'id': 1, 'name': 'one', 'parent': None}]
    response = client.get(reverse("category-detail", args=[category.id]))
    assert response.json() == {'id': 1, 'name': 'one', 'parent': None}


def test_category_create(client):
    assert Category.objects.count() == 0
    response = client.post("/category/", data={"name": "test"})
    assert response.status_code == 201
    assert response.json() == {'id': 1, 'name': 'test', 'parent': None}
    assert Category.objects.count() == 1


def test_category_update(client):
    category = Category.objects.create(name="one")
    url = reverse("category-detail", args=[category.id])
    response = client.put(
        url, data={"name": "test"}, content_type="application/json"
    )
    assert response.status_code == 200
    assert response.json() == {'id': 1, 'name': 'test', 'parent': None}
    assert Category.objects.filter(name="test").exists()


def test_category_delete(client):
    category = Category.objects.create(name="one")
    url = reverse("category-detail", args=[category.id])
    response = client.delete(
        url, content_type="application/json"
    )
    assert response.status_code == 204
    assert Category.objects.count() == 0

def test_category_parent_update(client):
    category_one = Category.objects.create(name="one")
    category_two = Category.objects.create(name="one", parent=category_one)
    url = reverse("category-detail", args=[category_two.id])
    assert not Category.objects.filter(parent=2).exists()
    response = client.patch(
        url, data={"parent": 2}, content_type="application/json"
    )
    assert response.status_code == 200
    assert response.json() == {'id': 2, 'name': 'one', 'parent': 2}
    assert Category.objects.filter(parent=2).exists()


def test_category_parents_list(client):
    category_one = Category.objects.create(name="one")
    category_two = Category.objects.create(name="two", parent=category_one)
    response = client.get(reverse("category_parents_list", args=[category_one.id]))
    assert response.json() == {
        'id': 1, 'name': 'one', 'children': [{'id': 2, 'name': 'two', 'children': []}]
    }


def test_category_product_offering_count_apiview(client):
    category = Category.objects.create(name="one")
    product = Product.objects.create(name="one", price=1)
    product.categories.add(category)
    # Use reverse to get the URL for the view
    url = reverse("category-product-offering-count-apiview")
    # Append the query parameter to the URL
    url_with_params = f"{url}?category_ids={category.id}"
    response = client.get(url_with_params)
    assert response.json() == [{'id': 1, 'name': 'one', 'num_products': 1}]
    product_two = Product.objects.create(name="two", price=1)
    product_two.categories.add(category)
    url_with_params = f"{url}?category_ids={category.id}"
    response = client.get(url_with_params)
    assert response.json() == [{'id': 1, 'name': 'one', 'num_products': 2}]


def test_category_product_total_offering_count_apiview(client):
    category = Category.objects.create(name="one")
    product = Product.objects.create(name="one", price=1)
    product.categories.add(category)
    # Use reverse to get the URL for the view
    url = reverse("category-product-total-offering-count-apiview")
    # Append the query parameter to the URL
    url_with_params = f"{url}?category_ids={category.id}"
    response = client.get(url_with_params)
    assert response.json() == {'num_products': 1}
    product_two = Product.objects.create(name="two", price=1)
    product_two.categories.add(category)
    url_with_params = f"{url}?category_ids={category.id}"
    response = client.get(url_with_params)
    assert response.json() == {'num_products': 2}
