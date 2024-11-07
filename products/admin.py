from django.contrib import admin
from products.models import Category,Product

@admin.register(Category)
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", )

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price")
    prepopulated_fields = {"slug": ["name"]}