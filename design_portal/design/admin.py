from django.contrib import admin
from .models import CustomUser
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name')  # Укажите поля для отображения в списке
    search_fields = ('username', 'email', 'first_name', 'last_name')  # Поля для поиска

admin.site.register(CustomUser, CustomUserAdmin)