from django.db import models
from peoples.models import Customer, Supplier
from owners.models import Owner
from products.models import Product
# Create your models here.

PAID_STATUS = [
    ("Paid", "Paid"),
    ("Unpaid", "Unpaid"),
]

class Purchase(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='purchases', null=False, blank=False)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='purchases')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='purchases', null=False, blank=False)
    quentity = models.IntegerField(default=0)
    purchase_date = models.DateField(auto_now_add=True)
    payable = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    paid = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    due = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)


class Sale(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='sales', null=False, blank=False)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='sales')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='sales', null=False, blank=False)
    quentity = models.IntegerField(default=0)
    date = models.DateField(auto_now_add=True)
    receivable = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    paid = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    due = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    purchase_cost = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    profit = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    status = models.CharField(choices=PAID_STATUS, max_length=15)

    
# today = date.today()
# from datetime import date