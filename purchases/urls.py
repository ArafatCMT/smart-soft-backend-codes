from django.urls import path
from . import views

urlpatterns = [
    path('product/', views.PurchaseView.as_view()),
    path('report/', views.AllPurchaseReportView.as_view()), # purchase report url

    path('sale/', views.SaleView.as_view()),
    path('sale/report/', views.AllSaleReportView.as_view()), 
    
]