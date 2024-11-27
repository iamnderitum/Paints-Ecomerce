from .models import Capacity, Category

def category_and_capacity_links(request):
    categories = Category.objects.all()
    capacities = Capacity.objects.all()

    return {
        "categories":categories,
        "capacities": capacities,
    }