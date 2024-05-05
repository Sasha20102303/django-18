from django.shortcuts import render
from.models import *
from django.core.paginator import Paginator

def index(request):
    context = {
    'title' : 'Рейх вещей',
    'index' : Product.objects.all(),
    'categories' : ProductCategory.objects.all()
    }
    return render(request, 'index.html', context = context)

def products(request ,category_id=None, page_namber=1):

    if category_id:
        products = Product.objects.fillter(category_id=category_id)
    else:
        products =Product.objects.all()
    per_page = 3 #сколько товара на одной странице
    paginator = Paginator(products, per_page)
    products_paginator = paginator.page(page_namber)

    context = {
        'title': 'Рейх вещей',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all()

    }

    return render(request, 'products.html', context)

def basket_add(request, product_id:id):

    product = Product.objects.get(id = product_id)
    baskets = Basket.objects.filter(user = request.user, product = product)

    if not baskets.exists():
        Basket.objects.create(user = request.user, product = product, quantity = 1)
    else:
        basket

def basket_remove(request, basket_id):
    basket = Basket.objects.get(id = basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


# Create your views here.
