from django.urls import path
from . import views

urlpatterns = [
    path('show/', views.ShowStockView.as_view()),
    
]