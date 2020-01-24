from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    ROLE = [("U", "User"),
            ("M", "Manager"),
            ]

    role = models.CharField(choices=ROLE, default=ROLE[0], verbose_name="Роль пользователя", max_length=4)

    REQUIRED_FIELDS = ['role', ]
