from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError


class Category(models.Model):
    name = models.CharField(max_length=30)
    parent = models.ForeignKey(
        "Category",
        on_delete=models.CASCADE, blank=True, null=True
    )

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name
    

@receiver(pre_save, sender=Category)
def valid_nested_parent_level(sender, instance, **kwargs):
    max_nested_level = 10

    if get_nesting_level(instance) > max_nested_level:
        raise ValidationError("Max value is 10")
    

def get_nesting_level(category):
    level = 0
    while category.parent:
        category = category.parent
        level += 1
    return level