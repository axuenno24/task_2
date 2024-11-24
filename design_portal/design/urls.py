from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),  # Главная страница
    path('register/', views.RegisterUser.as_view(), name='register'),  # Регистрация
    path('login/', views.LoginUser.as_view(), name='login'),  # Вход
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', views.ProfileUser.as_view(), name='profile'),  # Каталог
]
