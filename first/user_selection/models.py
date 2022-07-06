from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.
all_role = [('Пользователь', 'Пользователь'),
            ('менеджер', 'менеджер'),
            ('CRM - администратор', 'CRM - администратор')]

class User(AbstractBaseUser):
    role_choice = models.CharField(max_length=20, choices=all_role, verbose_name='роль')
    Offer = models.BooleanField(default=False)
    Avatar = models.ImageField(upload_to="photo_sales/%Y/%m/%d", blank=True, verbose_name='Аватар')

    def __str__(self):
        return self.role_choice
