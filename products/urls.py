from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("category/<slug:slug>/", views.category_detail, name="category_detail"),
    path("product/<slug:slug>/", views.product_detail, name="product_detail"),
]