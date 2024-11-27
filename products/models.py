from django.db import models
from ckeditor.fields import RichTextField
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
    description = RichTextField(default="Default catch phrase text")
    image = models.ImageField(upload_to="products/", null=True, blank=True)

    catch_phrase = RichTextField(default="Default catch phrase text")
    key_features = RichTextField(default="Default catch phrase text")
    why_choose =RichTextField(default="Default why choose text")

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



class BusinessContact(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    default_message = models.TextField(default="Hello, I'd Like to Enquire about The Zelco Products")
