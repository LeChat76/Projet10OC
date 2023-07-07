from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date


class Users(AbstractUser):
    username = models.CharField(
        max_length = 20,
        unique = True,
    )
    email = models.EmailField(
        max_length=255,
        unique=True,
    )
    birthday = models.DateField(null=True, blank=True, default=None)
    can_be_contacted = models.BooleanField(default=False)
    can_data_be_shared = models.BooleanField(default=False)

    def is_adult(self):
        today = date.today()
        age = today.year - self.birthday.year - ((today.month, today.day) < (self.birthday.month, self.birthday.day))
        return age >= 15

