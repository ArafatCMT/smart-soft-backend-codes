from django.shortcuts import render
from owners.models import Owner
from peoples import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from peoples.models import Customer, Supplier, CustomerDueReport, SupplierDueReport, Salary, Employee
from rest_framework.generics import ListAPIView
from rest_framework import filters
from django.http import Http404
from .permissions import IsAuthorOrReadOnly

# Customer
class CustomerView(APIView):
    serializer_class = serializers.CustomerSerializer

    def post(self, request, format=None):
        owner = Owner.objects.get(user = request.user)
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save(owner=owner)
            return Response({'details': 'customer added successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class EditCustomerView(APIView):
    permission_classes = [IsAuthorOrReadOnly]
    serializer_class = serializers.CustomerSerializer

    def get_objects(self, pk):
        try:
            return Customer.objects.get(pk=pk)
        except(Customer.DoesNotExist):
            raise Http404
    
    def get(self, request, pk, format=None):
        # print(request.user)
        customer = self.get_objects(pk)
        # serializer = self.serializer_class(post)
        serializer = self.serializer_class(customer)
        return Response(serializer.data)
        
    def put(self, request, pk, format=None):
        # print('edit by',request.user)
        customer = self.get_objects(pk)
        serializer = self.serializer_class(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'details': 'Edit successfully'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ShowCustomer(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        owner_id = request.query_params.get('owner_id')
        if owner_id:
            return queryset.filter(owner = owner_id)
        return queryset

class AllCustomerView(ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = serializers.CustomerSerializer
    filter_backends = [ShowCustomer]

#Supplier
class SupplierView(APIView):
    serializer_class = serializers.SupplierSerializer

    def post(self, request, format=None):
        owner = Owner.objects.get(user = request.user)
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save(owner=owner)
            return Response({'details': 'supplier added successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EditSupplierView(APIView):
    permission_classes = [IsAuthorOrReadOnly]
    serializer_class = serializers.SupplierSerializer

    def get_objects(self, pk):
        try:
            return Supplier.objects.get(pk=pk)
        except(Supplier.DoesNotExist):
            raise Http404
    
    def get(self, request, pk, format=None):
        # print(request.user)
        supplier = self.get_objects(pk)
        # serializer = self.serializer_class(post)
        serializer = self.serializer_class(supplier)
        return Response(serializer.data)
        
    def put(self, request, pk, format=None):
        # print('edit by',request.user)
        supplier = self.get_objects(pk)
        serializer = self.serializer_class(supplier, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'details': 'Edit successfully'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ShowSupplier(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        owner_id = request.query_params.get('owner_id')
        if owner_id:
            return queryset.filter(owner = owner_id)
        return queryset

class AllSupplierView(ListAPIView):
    queryset = Supplier.objects.all()
    serializer_class = serializers.SupplierSerializer
    filter_backends = [ShowSupplier]

# Employee

class EmployeeView(APIView):
    serializer_class = serializers.EmployeeSerializer

    def post(self, request, format=None):
        owner = Owner.objects.get(user = request.user)
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save(owner=owner)
            return Response({'details': 'supplier added successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EditEmployeeView(APIView):
    permission_classes = [IsAuthorOrReadOnly]
    serializer_class = serializers.EmployeeSerializer

    def get_objects(self, pk):
        try:
            return Employee.objects.get(pk=pk)
        except(Employee.DoesNotExist):
            raise Http404
    
    def get(self, request, pk, format=None):
        # print(request.user)
        employee = self.get_objects(pk)
        # serializer = self.serializer_class(post)
        serializer = self.serializer_class(employee)
        return Response(serializer.data)
        
    def put(self, request, pk, format=None):
        # print('edit by',request.user)
        supplier = self.get_objects(pk)
        serializer = self.serializer_class(supplier, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'details': 'Edit successfully'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ShowEmployee(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        owner_id = request.query_params.get('owner_id')
        if owner_id:
            return queryset.filter(owner = owner_id)
        return queryset

class AllEmployeeView(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer
    filter_backends = [ShowEmployee]


# Salary
class SalaryView(APIView):
    serializer_class = serializers.SalarySerializer

    def post(self, request, format=None):
        owner = Owner.objects.get(user=request.user)
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            employee = serializer.validated_data['employee']
            paid_amount = serializer.validated_data['paid_amount']
            obj = serializer.save(owner)

            emp = Employee.objects.get(id=employee.id)
            print(employee)
            print(emp)
            total_paid = emp.total_paid
            total_receiveable = emp.total_receivable
            salary = emp.salary
            total_due = emp.total_due

            if paid_amount < salary:
                emp.total_due += (salary - paid_amount)
            if salary < paid_amount:
                emp.total_due -= (paid_amount - salary)

            emp.total_paid += paid_amount
            emp.total_receivable += salary
            emp.save()
            
            return Response({'details': 'salary payment successfully'},status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ShowSalaryReport(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        owner_id = request.query_params.get('owner_id')
        if owner_id:
            return queryset.filter(owner = owner_id)
        return queryset

class AllSalaryReportView(ListAPIView):
    queryset = Salary.objects.all()
    serializer_class = serializers.SalarySerializer
    filter_backends = [ShowSalaryReport]    

class ShowCustomerDueReport(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        owner_id = request.query_params.get('owner_id')
        if owner_id:
            return queryset.filter(owner = owner_id)
        return queryset

class AllCustomerDueReportView(ListAPIView):
    queryset = CustomerDueReport.objects.all()
    serializer_class = serializers.CustomerDueReportSerializer
    filter_backends = [ShowCustomerDueReport]


class ShowSupplierDueReport(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        owner_id = request.query_params.get('owner_id')
        if owner_id:
            return queryset.filter(owner = owner_id)
        return queryset

class AllSupplierDueReportView(ListAPIView):
    queryset = SupplierDueReport.objects.all()
    serializer_class = serializers.SupplierDueReportSerializer
    filter_backends = [ShowSupplierDueReport]
