from django.db import models
from owners.models import Owner
from django.utils.text import slugify

# Create your models here.
class Category(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='category')
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    
class Brand(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='brands')
    name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name}"

class Unit(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name="units")
    name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name}"
    
class Product(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name="products")
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='products', null=True, blank=True)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name='products')
    sale_price = models.IntegerField()
    purchase_cost = models.IntegerField()

    def __str__(self):
        return f"{self.name}"
