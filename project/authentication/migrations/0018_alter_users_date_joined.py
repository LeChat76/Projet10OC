# Generated by Django 4.2.3 on 2023-07-12 14:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0017_alter_users_date_joined'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]