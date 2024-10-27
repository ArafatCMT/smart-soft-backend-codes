from django.shortcuts import render, redirect
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
from django.utils import timezone
from sslcommerz_lib import SSLCOMMERZ 
import uuid
import random
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def generate_transaction_id():
   transaction_id = random.randint(100000000000, 999999999999)
   return transaction_id

class PurchaseView(APIView):
    serializer_class = serializers.PurchaseSerializer

    def get_objects(self, id):
        try:
            return Owner.objects.get(id=id)
        except(Owner.DoesNotExist):
            raise None

    def post(self, request, id, format=None):
        owner = self.get_objects(id)
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
            return Response({'details': 'parchase successfully', 'id': purchase.id},status.HTTP_201_CREATED)
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
class TodayPurchaseView(APIView):
    serializer_class = serializers.PurchaseSerializer

    def get(self, request, id, format=None):
        owner = Owner.objects.get(id=id)
        today = timezone.now().date()
        print(today)
        purchase = models.Purchase.objects.filter(purchase_date=today)
        purchase = purchase.filter(owner=owner)
        print(purchase)
        serializer = serializers.PurchaseSerializer(purchase, many=True)
        return Response(serializer.data)
    
# Sale view

class SaleView(APIView):
    serializer_class = serializers.SaleSerializer

    def get_objects(self, id):
        try:
            return Owner.objects.get(id=id)
        except(Owner.DoesNotExist):
            raise None

    def post(self, request, id, format=None):
        owner = self.get_objects(id)
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
            return Response({'details': 'sale successfully', 'id': sale.id},status.HTTP_201_CREATED)
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


class TodaySaleView(APIView):
    serializer_class = serializers.SaleSerializer

    def get(self, request, id, format=None):
        owner = Owner.objects.get(id=id)
        today = timezone.now().date()
        sale = models.Sale.objects.filter(date=today)
        sale = sale.filter(owner=owner)
        serializer = serializers.SaleSerializer(sale, many=True)
        return Response(serializer.data)



def payment(request, pk, page_nm):

    # owner = models.Owner.objects.get(pk=pk)
    # print(owner)
    if page_nm == 2:
        sale = models.Sale.objects.get(id=pk)

        settings = { 'store_id': 'smart671d117e7a816', 'store_pass': 'smart671d117e7a816@ssl', 'issandbox': True }
        sslcz = SSLCOMMERZ(settings)
        post_body = {}
        post_body['total_amount'] = sale.paid
        post_body['currency'] = "BDT"
        post_body['tran_id'] = generate_transaction_id()
        post_body['success_url'] = f'https://smart-soft-gold.vercel.app/purchases/payment/{pk}/{page_nm}/'
        post_body['fail_url'] = f'https://smart-soft-gold.vercel.app/purchases/payment/{pk}/{page_nm}/'
        post_body['cancel_url'] = f'https://smart-soft-gold.vercel.app/purchases/payment/{pk}/{page_nm}/'
        post_body['emi_option'] = 0
        post_body['cus_name'] = f'{sale.customer.name}'
        post_body['cus_email'] = f'{sale.customer.email}'
        post_body['cus_phone'] = f'{sale.customer.phone}'
        post_body['cus_add1'] = f'{sale.customer.address}'
        post_body['cus_city'] = "Dhaka"
        post_body['cus_country'] = "Bangladesh"
        post_body['shipping_method'] = "NO"
        post_body['multi_card_name'] = ""
        post_body['num_of_item'] = 1
        post_body['product_name'] = f'{sale.product.name}'
        post_body['product_category'] = f'{sale.product.category}'
        post_body['product_profile'] = "general"


        response = sslcz.createSession(post_body) # API response
        # print(response)
        return redirect(response['GatewayPageURL'])
    if page_nm == 3:
        pur = models.Purchase.objects.get(id=pk)

        settings = { 'store_id': 'smart671d117e7a816', 'store_pass': 'smart671d117e7a816@ssl', 'issandbox': True }
        sslcz = SSLCOMMERZ(settings)
        post_body = {}
        post_body['total_amount'] = pur.paid
        post_body['currency'] = "BDT"
        post_body['tran_id'] = generate_transaction_id()
        post_body['success_url'] = f'https://smart-soft-gold.vercel.app/purchases/payment/{pk}/{page_nm}/'
        post_body['fail_url'] = f'https://smart-soft-gold.vercel.app/purchases/payment/{pk}/{page_nm}/'
        post_body['cancel_url'] = f'https://smart-soft-gold.vercel.app/purchases/payment/{pk}/{page_nm}/'
        post_body['emi_option'] = 0
        post_body['cus_name'] = f'{pur.supplier.name}'
        post_body['cus_email'] = f'{pur.supplier.email}'
        post_body['cus_phone'] = f'{pur.supplier.phone}'
        post_body['cus_add1'] = f'{pur.supplier.address}'
        post_body['cus_city'] = "Dhaka"
        post_body['cus_country'] = "Bangladesh"
        post_body['shipping_method'] = "NO"
        post_body['multi_card_name'] = ""
        post_body['num_of_item'] = 1
        post_body['product_name'] = f'{pur.product.name}'
        post_body['product_category'] = f'{pur.product.category}'
        post_body['product_profile'] = "general"


        response = sslcz.createSession(post_body) # API response
        # print(response)
        return redirect(response['GatewayPageURL'])

@csrf_exempt
def payment_successfull(request, id, page_nm):
    print(page_nm)
    if page_nm == 2:
        sale = models.Sale.objects.get(id=id)
        sale.isPayment = True
        sale.save()
        return redirect('https://arafatcmt.github.io/smart_soft-frontend-codes/sale.html?id=2')
    if page_nm == 3:
        purchase = models.Purchase.objects.get(id=id)
        purchase.isPayment = True
        purchase.save()
        return redirect('https://arafatcmt.github.io/smart_soft-frontend-codes/purchase.html?id=3')

