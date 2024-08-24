from django.urls import path
from . import views

urlpatterns = [
    path('add/category/', views.CategoryView.as_view()),
    path('all/category/', views.AllCategoryView.as_view()),
    path('category/<int:id>/', views.CategoryWiseProductView.as_view()),

    path('add/product/', views.ProductView.as_view()),
    path('all/product/', views.AllProductView.as_view()),

    path('add/brand/', views.BrandView.as_view()),
    path('all/brand/', views.AllBrandView.as_view()),
    path('brand/<int:id>/', views.BrandWiseProductView.as_view()),

    path('add/unit/', views.UnitView.as_view()),
    path('all/unit/', views.AllUnitView.as_view()),
]