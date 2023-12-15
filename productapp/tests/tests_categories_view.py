import pytest
import json
from django.urls import reverse

from productapp.models import Category

pytestmark = pytest.mark.django_db


def test_category_list(client):
    category = Category.objects.create(name="one")
    response = client.get(reverse("category-list"))
    assert response.json() == [{'id': 1, 'name': 'one'}]
    response = client.get(reverse("category-detail", args=[category.id]))
    assert response.json() == {'id': 1, 'name': 'one'}


def test_category_create(client):
    assert Category.objects.count() == 0
    response = client.post("/category-list/", data={"name": "test"})
    assert response.status_code == 201
    assert response.json() == {'id': 1, 'name': 'test'}
    assert Category.objects.count() == 1


def test_category_update(client):
    category = Category.objects.create(name="one")
    url = reverse("category-detail", args=[category.id])
    response = client.put(
        url, data={"name": "test"}, content_type="application/json"
    )
    assert response.status_code == 200
    assert response.json() == {'id': 1, 'name': 'test'}
    assert Category.objects.filter(name="test").exists()


def test_category_delete(client):
    category = Category.objects.create(name="one")
    url = reverse("category-detail", args=[category.id])
    response = client.delete(
        url, content_type="application/json"
    )
    assert response.status_code == 204
    assert Category.objects.count() == 0
