from django.db import models
from products.models import Product
from owners.models import Owner
# Create your models here.
class Stock(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, null=True, blank=True)
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    purchase = models.IntegerField(default=0)
    sold = models.IntegerField(default=0)
    available_stock = models.IntegerField(default=0)
    sale_value = models.IntegerField(default=0)
    purchase_value = models.IntegerField(default=0)