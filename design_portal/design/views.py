from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.views import generic, View
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import LoginForm, RegisterUserForm


# Главная страница
def index(request):
    return render(request, 'index.html')


# Регистрация
class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'registration/register.html'
    extra_context = {'title': "Register"}
    success_url = reverse_lazy('login')


class LoginUser(LoginView):
    form_class = LoginForm
    template_name = 'registration/login.html'
    extra_context = {'title': 'Авторизация'}


# Выход
def logout_view(request):
    logout(request)  # Выход пользователя
    return render(request, 'registration/logout.html')

# Профиль
# def profile(request):
#     # Получаем текущего пользователя
#     user = request.user
#
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST, instance=user)
#         if form.is_valid():
#             form.save()
#             return redirect(
#                 reverse_lazy('registration:profile'))  # Перенаправление на профиль после успешного сохранения
#     else:
#         form = CustomUserCreationForm(instance=user)  # Инициализация формы с данными пользователя
#
#     return render(request, 'catalog/profile.html', {'form': form})
