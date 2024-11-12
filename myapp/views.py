from django.shortcuts import render, get_object_or_404
from datetime import datetime
from .models import *


# Create your views here.
# def home(request):
#     featured_products = Product.objects.filter(stock__gt=0)[:6]
#     categories = Category.objects.all()
#     return render(request, 'base.html', {
#         'year': datetime.now().year,
#         'featured_products': featured_products,
#         'categories': categories
#     })
def home(request):
    products = Product.objects.all()  # Fetch all products from the database
    return render(request, 'home.html', {
        'year': datetime.now().year,
        'products': products
    })
    
        
def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.all()

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'products': products
    }
    return render(request, 'product_list.html', context)


def product_details(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'product_details.html', {'product': product})
