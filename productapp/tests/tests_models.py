import pytest

from django.core.exceptions import ValidationError

from productapp.models import Category

pytestmark = pytest.mark.django_db


@pytest.fixture
def ten_nested_categories():
    category_one = Category.objects.create(name="one")
    category_two = Category.objects.create(name="two", parent=category_one)
    category_three = Category.objects.create(name="three", parent=category_two)
    category_four = Category.objects.create(name="four", parent=category_three)
    category_five = Category.objects.create(name="five", parent=category_four)
    category_six = Category.objects.create(name="six", parent=category_five)
    category_seven = Category.objects.create(name="seven", parent=category_six)
    category_eight = Category.objects.create(name="eight", parent=category_seven)
    category_nine = Category.objects.create(name="nine", parent=category_eight)
    category_ten = Category.objects.create(name="ten", parent=category_nine)
    category_eleven = Category.objects.create(name="eleven", parent=category_ten)
    return category_eleven


def test_category_parent(ten_nested_categories):
    assert Category.objects.count() == 11


def test_category_limit(ten_nested_categories):
    category_eleven = ten_nested_categories
    with pytest.raises(Exception) as exc_info:
        Category.objects.create(name="eleven", parent=category_eleven)
    assert exc_info.type == ValidationError
    assert exc_info.value.message == "Max value is 10"
