from django.db import models
from owners.models import Owner
# Create your models here.

class Customer(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='customers')
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=12)
    address = models.TextField(null=True, blank=True)
    receivable = models.DecimalField(max_digits=12, decimal_places=2, default=0.00, null=True, blank=True)
    paid = models.DecimalField(max_digits=12, decimal_places=2, default=0.00, null=True, blank=True)
    sale_due = models.DecimalField(max_digits=12, decimal_places=2, default=0.00, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"
    
class Supplier(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='suppliers')
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=12)
    address = models.TextField(null=True, blank=True)
    payable = models.DecimalField(max_digits=12, decimal_places=2, default=0.00, null=True, blank=True)
    paid = models.DecimalField(max_digits=12, decimal_places=2, default=0.00, null=True, blank=True)
    purchase_due = models.DecimalField(max_digits=12, decimal_places=2, default=0.00, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"
    
class Employee(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='employees')
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=12)
    address = models.TextField(null=True, blank=True)
    joining_date = models.DateField(auto_now_add=True)
    salary = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    total_receivable = models.DecimalField(max_digits=12, decimal_places=2 , default=0.00)
    total_paid = models.DecimalField(max_digits=12, decimal_places=2 , default=0.00)
    total_due = models.DecimalField(max_digits=12, decimal_places=2 , default=0.00)

    def __str__(self):
        return f"{self.name}"
    

class Salary(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='salarys', null=True, blank=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='salarys')
    paid_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.employee.name}"
    
class CustomerDueReport(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    total_due = models.IntegerField(default=0)

class SupplierDueReport(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    supplier = models.OneToOneField(Supplier, on_delete=models.CASCADE)
    total_due = models.IntegerField(default=0)

