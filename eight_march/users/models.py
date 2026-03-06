from django.contrib.auth.models import AbstractUser
from django.db import models


class MyUser(AbstractUser):
    bio = models.TextField(
        verbose_name='Биография',
        max_length=256,
        blank=True
    )
