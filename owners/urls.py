from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.RegistrationView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('verify/<uid64>/<token>/', views.is_active),

    path('profile/', views.ProfileView.as_view()),
    path('user/', views.UserView.as_view()),
]