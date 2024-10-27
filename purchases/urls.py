from django.urls import path
from . import views

urlpatterns = [
    path('product/<int:id>/', views.PurchaseView.as_view()),
    path('today/<int:id>/', views.TodayPurchaseView.as_view()),
    path('report/', views.AllPurchaseReportView.as_view()), # purchase report url

    path('sale/<int:id>/', views.SaleView.as_view()),
    path('sale/report/', views.AllSaleReportView.as_view()), 
    path('sale/today/<int:id>/', views.TodaySaleView.as_view()),

    path('pay/<int:pk>/<int:page_nm>/', views.payment),
    path('payment/<int:id>/<int:page_nm>/', views.payment_successfull),
    
]