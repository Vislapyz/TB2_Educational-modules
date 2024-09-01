from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    """Cоздания модели Пользователя"""
    username = None

    email = models.EmailField(unique=True, verbose_name='Email')
    name = models.CharField(max_length=50, verbose_name="Имя", **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
