from django.contrib import admin
from products.models import Category,Product,BusinessContact

@admin.register(Category)
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", )
    prepopulated_fields = {"slug": ["name"]}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price")
    prepopulated_fields = {"slug": ["name"]}


@admin.register(BusinessContact)
class BusinessContactAdmin(admin.ModelAdmin):
    list_display = ("name", "phone_number")