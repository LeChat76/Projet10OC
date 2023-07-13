from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):

    def __str__(self):
        return f'username : {self.username} / id : {self.id}'

    # disable fields not needed in this project
    email, first_name, last_name, last_login = None, None, None, None

    username = models.CharField(
        max_length = 20,
        unique = True,
    )
    date_joined = models.DateTimeField(default=timezone.now)
    birthday = models.DateField(default=None)
    can_be_contacted = models.BooleanField(default=False)
    can_data_be_shared = models.BooleanField(default=False)


