from django.db import models
from django.contrib.auth.models import AbstractUser



class CustomUser(AbstractUser):
    username = models.CharField(max_length=100, verbose_name='Имя пользователя', unique=True)
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    email = models.EmailField(max_length=100, verbose_name='Email', unique=True)
    password = models.CharField(max_length=100, verbose_name='Пароль')
    password_confirm = models.CharField(max_length=100, verbose_name='Подтверждение пароля' )

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Уникальное имя для этой связи
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',  # Уникальное имя для этой связи
        blank=True,
    )

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username

