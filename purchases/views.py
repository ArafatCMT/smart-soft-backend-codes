from django.shortcuts import render
from . import serializers
from . import models
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework import filters
from owners.models import Owner
from rest_framework.response import Response
from rest_framework import status
from products.models import Product
from stocks.models import Stock
# from peoples import models
from peoples.models import SupplierDueReport, Supplier, Customer, CustomerDueReport
from . import models
# Create your views here.

class PurchaseView(APIView):
    serializer_class = serializers.PurchaseSerializer

    def post(self, request, format=None):
        owner = Owner.objects.get(user = request.user)
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            supplier = serializer.validated_data['supplier']
            product = serializer.validated_data['product']
            quentity = serializer.validated_data['quentity']
            payable = serializer.validated_data['payable']
            paid = serializer.validated_data['paid']
            purchase = serializer.save(owner)

            if  purchase.due > 0:
                # bokeya raktaci
                try:
                    due_repot = SupplierDueReport.objects.get(supplier=supplier)
                except(SupplierDueReport.DoesNotExist):
                    due_repot = None
                
                if due_repot:
                    # supplier er kace bokeya thakle ,  total_bokeya er shathe notun bokeya add kortaci
                    due_repot.total_due += purchase.due
                    due_repot.save()
                else:
                    # supplier er kace bokeya nai ty notun er bokeya ta raktaci tar ak ta report toiri korta ci
                    supplier_due_report = SupplierDueReport.objects.create(owner=owner, supplier=supplier, total_due=purchase.due)
                    supplier_due_report.save()
            if  payable < paid:
                try:
                    due_repot = SupplierDueReport.objects.get(supplier=supplier)
                except(SupplierDueReport.DoesNotExist):
                    due_repot = None

                if due_repot:
                    # supplier er kace bokeya thakle ,  total_bokeya er shathe notun bokeya add kortaci
                    due_repot.total_due -= (paid - payable)
                    due_repot.save()
                if due_repot.total_due == 0:
                    due_repot.delete()
                
            # print(due_repot.supplier.name, due_repot.id)
            # print(supplier, supplier.id)
            supp = Supplier.objects.get(id=supplier.id)
            prod = Product.objects.get(id=product.id)
            # add supplier list
            if paid > payable:
                supp.purchase_due -= (paid - payable)
            if payable > paid:
                supp.purchase_due += (payable - paid)
            supp.payable += payable
            supp.paid += paid
            supp.save()

            # stock e add
            stock = Stock.objects.get(product=product)
            stock.purchase += quentity
            stock.sale_value += (quentity * prod.sale_price) 
            stock.purchase_value += (quentity * prod.purchase_cost)
            stock.available_stock += quentity
            stock.save()
            return Response({'details': 'parchase successfully'},status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ShowPurchaseReport(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        owner_id = request.query_params.get('owner_id')
        if owner_id:
            return queryset.filter(owner = owner_id)
        return queryset

class AllPurchaseReportView(ListAPIView):
    queryset = models.Purchase.objects.all()
    serializer_class = serializers.PurchaseSerializer
    filter_backends = [ShowPurchaseReport]

# Sale view
class SaleView(APIView):
    serializer_class = serializers.SaleSerializer

    def post(self, request, format=None):
        owner = Owner.objects.get(user = request.user)
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            customer = serializer.validated_data['customer']
            product = serializer.validated_data['product']
            quentity = serializer.validated_data['quentity']
            receivable = serializer.validated_data['receivable']
            paid = serializer.validated_data['paid']
            sale = serializer.save(owner)

            if  sale.due > 0:
                # bokeya raktaci
                try:
                    due_repot = CustomerDueReport.objects.get(customer=customer)
                except(CustomerDueReport.DoesNotExist):
                    due_repot = None
                
                if due_repot:
                    # customer er thake bokeya thakle ,  total_bokeya er shathe notun bokeya add kortaci
                    due_repot.total_due += sale.due
                    due_repot.save()
                else:
                    # customer er kace bokeya nai ty notun er bokeya ta raktaci tar ak ta report toiri korta ci
                    customer_due_report = CustomerDueReport.objects.create(owner=owner, customer=customer, total_due=sale.due)
                    customer_due_report.save()

            if  receivable < paid:
                try:
                    due_repot = CustomerDueReport.objects.get(customer=customer)
                except(CustomerDueReport.DoesNotExist):
                    due_repot = None

                if due_repot:
                    # customer er  bokeya thakle ,  total_bokeya er shathe extra taka bad deye dicci
                    due_repot.total_due -= (paid - receivable)
                    due_repot.save()
                if due_repot.total_due == 0:
                    due_repot.delete()
                
            
            cust = Customer.objects.get(id=customer.id)
            prod = Product.objects.get(id=product.id)
            # add customer list
            if paid > receivable:
                cust.sale_due -= (paid - receivable)
            if receivable > paid:
                cust.sale_due += (receivable - paid)
            cust.receivable += receivable
            cust.paid += paid
            cust.save()

            # stock e add
            stock = Stock.objects.get(product=product)
            stock.sold += quentity
            stock.sale_value -= (quentity * prod.sale_price) 
            stock.purchase_value -= (quentity * prod.purchase_cost)
            stock.available_stock -= quentity
            stock.save()
            return Response({'details': 'parchase successfully'},status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ShowSaleReport(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        owner_id = request.query_params.get('owner_id')
        if owner_id:
            return queryset.filter(owner = owner_id)
        return queryset

class AllSaleReportView(ListAPIView):
    queryset = models.Sale.objects.all()
    serializer_class = serializers.SaleSerializer
    filter_backends = [ShowSaleReport]


