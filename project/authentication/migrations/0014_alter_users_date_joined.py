# Generated by Django 4.2.3 on 2023-07-10 16:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0013_alter_users_date_joined'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 10, 18, 41, 12, 270920)),
        ),
    ]
