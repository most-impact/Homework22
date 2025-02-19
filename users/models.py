from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Email')
    phone = models.CharField(max_length=35, verbose_name='Номер телефона', blank=True, null=True,
                             help_text='Введите номер телефона')
    tg_name = models.CharField(max_length=50, verbose_name='Ник телеграм', blank=True, null=True,
                             help_text='Введите ник телеграмма')
    avatar = models.ImageField(upload_to='users/avatars/', verbose_name='Аватар', blank=True, null=True,
                             help_text='Загрузите свой аватар')
    token = models.CharField(max_length=100, verbose_name='Token',blank=True, null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
