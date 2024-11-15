from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views import generic, View

from .forms import LoginForm, CustomUserCreationForm
from django.urls import reverse_lazy

# Главная страница
def index(request):
    return render(request, 'index.html')

# Регистрация
class Registration(generic.CreateView):
    templates_name = 'registration/register.html'
    form_class = CustomUserCreationForm
    transition_url = reverse_lazy("register")

# Вход
class Login(View):
    template_name = 'registration/login.html'
    form_class = LoginForm

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')
        form = self.form_class()  # Пустая форма для GET-запроса
        return render(request, self.template_name, {'form': form})


# Выход
def logout_view(request):
    logout(request)  # Выход пользователя
    return redirect('index')

# Профиль
def profile(request):
    return render(request, 'registration/profile.html')
