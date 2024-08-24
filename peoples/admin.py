from django.contrib import admin
from .models import Customer, Supplier, Employee, Salary, CustomerDueReport, SupplierDueReport
# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['owner','name', 'email', 'phone', 'address', 'receivable', 'paid', 'sale_due']

class SupplierAdmin(admin.ModelAdmin):
    list_display = ['owner','name', 'email', 'phone', 'address', 'payable', 'paid', 'purchase_due']

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['owner','name', 'email', 'phone', 'address', 'salary', 'joining_date', 'total_receivable', 'total_paid', 'total_due']

class SalaryAdmin(admin.ModelAdmin):
    list_display = ['owner','name', 'email', 'address', 'phone', 'total_receivable' , 'paid_amount', 'date']

    def name(self, obj):
        return f"{obj.employee.name}"
    
    def email(self, obj):
        return f"{obj.employee.email}"
    
    def address(self, obj):
        return f"{obj.employee.address}"
    
    def phone(self, obj):
        return f"{obj.employee.phone}"
    
    def total_receivable(self, obj):
        return f"{obj.employee.salary}"

class CustomerDueReportAdmin(admin.ModelAdmin):
    list_display = ['owner','name', 'email', 'address', 'phone', 'total_due']

    def name(self, obj):
        return f"{obj.customer.name}"
    
    def email(self, obj):
        return f"{obj.customer.email}"
    
    def address(self, obj):
        return f"{obj.customer.address}"
    
    def phone(self, obj):
        return f"{obj.customer.phone}"
    
class SupplierDueReportAdmin(admin.ModelAdmin):
    list_display = ['owner', 'name', 'email', 'phone', 'address', 'total_due']

    def name(self, obj):
        return f"{obj.supplier.name}"
    
    def email(self, obj):
        return f"{obj.supplier.email}"
    
    def address(self, obj):
        return f"{obj.supplier.address}"
    
    def phone(self, obj):
        return f"{obj.supplier.phone}"


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Supplier, SupplierAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Salary, SalaryAdmin)
admin.site.register(CustomerDueReport, CustomerDueReportAdmin)
admin.site.register(SupplierDueReport, SupplierDueReportAdmin)
