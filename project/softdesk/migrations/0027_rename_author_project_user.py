# Generated by Django 4.2.3 on 2023-07-13 12:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('softdesk', '0026_rename_user_project_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='author',
            new_name='user',
        ),
    ]
