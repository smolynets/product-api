from django.contrib import admin
from productapp.models import Category, Product

class CategoryAdmin(admin.ModelAdmin):
    fields = ("name", "parent")
    list_display = ("name", "parent")


class ProductInline(admin.TabularInline):
    model = Product.categories.through


class ProductAdmin(admin.ModelAdmin):
    fields = ("name", "price")
    list_display = ("name", "price", "get_categories")
    filter_horizontal = ('categories',)

    inlines = [
        ProductInline,
    ]

    def get_categories(self, obj):
        return [p.name for p in obj.categories.all()]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
