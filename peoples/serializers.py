from rest_framework import serializers
from peoples import models

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Customer
        fields = ['id', 'owner', 'name', 'email', 'phone', 'address', 'receivable', 'paid', 'sale_due']
        read_only_fields = ['owner', 'receivable', 'paid', 'sale_due']


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Supplier
        fields = ['id','owner', 'name', 'email', 'phone', 'address', 'payable', 'paid', 'purchase_due']
        read_only_fields = ['owner', 'payable', 'paid', 'purchase_due']

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta: 
        model = models.Employee
        fields = ['id', 'owner', 'name', 'email', 'phone', 'address', 'joining_date', 'salary', 'total_receivable', 'total_paid', 'total_due']
        read_only_fields = ['owner', 'total_receivable', 'total_paid', 'total_due']

class SalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Salary
        fields = ['id','owner', 'employee', 'paid_amount', 'date']
        read_only_fields = ['owner']

    def save(self, owner):
        employee = self.validated_data['employee']
        paid_amount = self.validated_data['paid_amount']

        if paid_amount <= 0:
            raise serializers.ValidationError({'error': "Invalid amount"})
        
        obj = models.Salary.objects.create(owner=owner, employee=employee, paid_amount=paid_amount)
        obj.save()
        return obj
        
        

class CustomerDueReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomerDueReport
        fields = ['id','owner', 'customer', 'total_due']
        read_only_fields = ['owner']

class SupplierDueReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SupplierDueReport
        fields = ['id','owner', 'supplier', 'total_due']
        read_only_fields = ['owner']


