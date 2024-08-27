from django.urls import path
from . import views

urlpatterns = [
    path('show/', views.ShowStockView.as_view()),
    path('check/<int:id>/', views.CheckStockView.as_view()),
    
]