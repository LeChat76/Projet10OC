# Generated by Django 4.2.3 on 2023-07-12 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('softdesk', '0018_alter_project_project_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='project_author',
            new_name='author_user_id',
        ),
    ]
