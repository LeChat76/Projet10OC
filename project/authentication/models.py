from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date, datetime


class Users(AbstractUser):

    def __str__(self):
        return self.username.capitalize()

    # disable fields not needed in this project
    email, first_name, last_name, last_login = None, None, None, None

    username = models.CharField(
        max_length = 20,
        unique = True,
    )
    birthday = models.DateField(default=None)
    # date_joined = models.DateTimeField(default=datetime.now())
    can_be_contacted = models.BooleanField(default=False)
    can_data_be_shared = models.BooleanField(default=False)

    def is_adult(self):
        today = date.today()
        age = today.year - self.birthday.year - ((today.month, today.day) < (self.birthday.month, self.birthday.day))
        return age >= 15

