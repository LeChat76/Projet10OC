# Generated by Django 4.2.3 on 2023-07-10 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0007_remove_users_email_alter_users_birthday'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='users',
            name='last_name',
        ),
    ]
