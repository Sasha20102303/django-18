from django.urls import path
from .views import *
app_name = 'products'

urlpatterns = [
    path('', products, name = 'index'),
    path('baskets/add/<int:product_id/', basket_add, name = 'basket_add')
]
