from django.urls import path
from . import views

urlpatterns = [
    path('add/category/<int:id>/', views.CategoryView.as_view()),
    path('all/category/', views.AllCategoryView.as_view()),
    path('category/<int:id>/', views.CategoryWiseProductView.as_view()),
    path('cat/<int:id>/', views.SingleCategoryView.as_view()),

    path('add/product/<int:id>/', views.ProductView.as_view()),
    path('all/product/', views.AllProductView.as_view()),
    path('single/product/<int:id>/', views.SingleProductView.as_view()),

    path('add/brand/<int:id>/', views.BrandView.as_view()),
    path('all/brand/', views.AllBrandView.as_view()),
    path('brands/<int:id>/', views.BrandWiseProductView.as_view()),
    path('brand/<int:id>/', views.SingleBrandView.as_view()),

    path('add/unit/<int:id>', views.UnitView.as_view()),
    path('all/unit/', views.AllUnitView.as_view()),
    path('unit/<int:id>/', views.SingleUnitView.as_view()),
]