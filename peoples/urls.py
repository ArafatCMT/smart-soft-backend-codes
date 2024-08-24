from django.urls import path
from . import views

urlpatterns = [
    path('add/customer/', views.CustomerView.as_view()),
    path('edit/customer/<int:pk>/', views.EditCustomerView.as_view()),
    path('all/customer/', views.AllCustomerView.as_view()),

    path('add/supplier/', views.SupplierView.as_view()),
    path('edit/supplier/<int:pk>/', views.EditSupplierView.as_view()),
    path('all/supplier/', views.AllSupplierView.as_view()),

    path('add/employee/', views.EmployeeView.as_view()),
    path('edit/employee/<int:pk>/', views.EditEmployeeView.as_view()),
    path('all/employee/', views.AllEmployeeView.as_view()),

    path('salary/', views.SalaryView.as_view()),
    path('salary/report/', views.AllSalaryReportView.as_view()),

    path('customer/due/report/', views.AllCustomerDueReportView.as_view()),
    path('supplier/due/report/', views.AllSupplierDueReportView.as_view()),
    
]