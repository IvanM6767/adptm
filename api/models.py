from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_ADMIN = 'admin'
    ROLE_USER = 'user'
    ROLE_CHOICES = (
        (ROLE_ADMIN, 'Администратор'),
        (ROLE_USER, 'Пользователь'),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=ROLE_USER)

    def __str__(self):
        return self.username