from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    code = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/category/{self.slug}/"

class Product(models.Model):
    name = models.CharField(max_length=50, null=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=True
    )
    price = models.CharField(max_length=50, null=True)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to="products/", null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/product/{self.slug}/"


class Capacity(models.Model):
    value = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(unique=True, null=True, blank=True)

    def __str__(self):
        return self.value

    def get_absolute_url(self):
        return f"/capacity/{self.slug}/"