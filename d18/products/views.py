from django.shortcuts import render
from.models import *

def index(request):
    context = {
    'title' : 'Рейх вещей',
    'index' : Product.objects.all(),
    'categories' : ProductCategory.objects.all()
    }
    return render(request, 'index.html', context = context)

def products(request):
    context = {
        'title': 'Рейх вещей',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all()

    }

    return render(request, 'products.html', context = context)








# Create your views here.
