from django.shortcuts import render
from.models import *

def index(request):
    context = {
    'title': 'Рейх вещей',
     'products' : Product.objects.all(),
     'categories' : ProductCategory.objects.all()
    }
    return render(request, 'index.html', context = context)

def products(request):
    context = {
        'products' : [
            {'image':'/static/vendor/img/products/Adidas-hoodie.png',
             'name':'Худи черного цвета с монограммами Adidas Originals',
             'price':'6 090,00 руб.',
             'description': 'Мягкая ткань для свитшотов. Стиль и комфорт - это образ жизни.'},

            {'image': '/static/vendor/img/products/Blue-jacket-The-North-Face.png',
             'name': 'Синяя куртка The North Face',
             'price': '23 725,00 руб.',
             'description': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель..'},

            {'image': '/static/vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png',
             'name': 'Коричневый спортивный oversized-топ ASOS DESIGN',
             'price': '3 390,00 руб.',
             'description': 'Материал с плюшевой текстурой. Удобный и мягкий.'},

            {'image': '/static/vendor/img/products/Black-Nike-Heritage-backpack.png',
             'name': 'Черный рюкзак Nike Heritage',
             'price': '2 340,00 руб.',
             'description': 'Плотная ткань. Легкий материал.'},

            {'image': '/static/vendor/img/products/Black-Dr-Martens-shoes.png',
             'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex',
             'price': '13 590,00 руб.',
             'description': 'Гладкий кожаный верх. Натуральный материал.'},

            {'image': '/static/vendor/img/products/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png',
             'name': 'Темно-синие широкие строгие брюки ASOS DESIGN',
             'price': '2 890,00 руб.',
             'description': 'Легкая эластичная ткань сирсакер Фактурная ткань.'},

            {'image': '/static/vendor/img/products/1648677871_5-kartinkof-club-p-reituzi-kartinki-smeshnie-5.jpg',
             'name': 'Зимние мужские рейтузы Alfa samets',
             'price': '9 000 000,00',
             'description': 'Теплые зимние рейтузы сделанные из бороды Дяди Васи'}




        ]

    }

    return render(request, 'products.html', context = context)








# Create your views here.
