# Generated by Django 4.2.3 on 2023-07-22 19:57

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('softdesk', '0048_alter_comment_issue_alter_contributor_project_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
