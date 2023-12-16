import pytest
import json
from django.urls import reverse

from productapp.models import Category

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
