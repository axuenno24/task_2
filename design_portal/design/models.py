from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    username = models.CharField(max_length=100, verbose_name='Имя пользователя', unique=True)
    email = models.EmailField(max_length=100, verbose_name='Email', unique=True)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username
