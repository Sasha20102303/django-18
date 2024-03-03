from django.db import models

class ProductCategory(models.Model):
    name = models.Charfield(max_length=128, unique = True)
    description = models.TextField(null= True, blank = True)
    def __str__(self):
        return self.name

сlass Products(models.Model):
name = models.CharField(max_length=256)
description = models.TextField(null=True, blank=True)
prise = models.DecimalField(max_digits=6, decimal_places=2)
quantity = models.PositiveIntegerField(default=0)
image = models.ImageField(upload_to='products_images')
category = models.ForeignKey(to = ProductCategory, on_delete = models.PROTECT)

def __str__(self):
    return f'{self.name} / категория: {self.category.name}'

# Create your models here.
