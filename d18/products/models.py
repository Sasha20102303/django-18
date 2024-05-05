from django.db import models

from users.models import User

class ProductCategory(models.Model):
    name = models.CharField(max_length=128, unique = True)
    description = models.TextField(null= True, blank = True)
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(null=True, blank=True)
    prise = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='products_images')
    category = models.ForeignKey(to = ProductCategory, on_delete = models.PROTECT)

    def __str__(self):
        return f'{self.name} / категория: {self.category.name}'




class Baskets(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    #кол-во в корзине
    quantity = models.PositiveSmallIntegerField(default=0)
    #запись даты и времени создания объекта
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Корзина для {self.user.username} | Продукт: {self.product.name}'






    def sum(self):
        return self.product.price * self.quantity


# Create your models here.
