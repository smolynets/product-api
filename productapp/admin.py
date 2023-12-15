from django.contrib import admin
from productapp.models import Category

class CategoryAdmin(admin.ModelAdmin):
    fields = ("name", "parent")
    list_display = ("name", "parent")


admin.site.register(Category, CategoryAdmin)
