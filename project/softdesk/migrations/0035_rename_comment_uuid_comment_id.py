# Generated by Django 4.2.3 on 2023-07-19 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('softdesk', '0034_remove_comment_id_comment_comment_uuid_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment_uuid',
            new_name='id',
        ),
    ]
