from django.shortcuts import render, get_object_or_404
from .models import Product, Category
# Create your views here.

def index(request):
    products = Product.objects.all()
    context = {
        "products":products
    }
    return render(request, "index-1.html", context)

def shop(request):
    products = Product.objects.all()
    context = {
        "products":products
    }
    return render(request, "products.html", context)
def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = category.products.all()
    return render(request, "shop/category_detail.html", {"category": category, "products": products})

def product_detail(request, slug):
    products = Product.objects.all()
    product = get_object_or_404(Product, slug=slug)
    return render(request, "product-detail.html", {"product": product, "products":products})

def error_404(request):
    return render (request, "404.html")

def contact(request):
    return render(request, "contact.html")