# Generated by Django 4.2.3 on 2023-07-22 19:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('softdesk', '0047_alter_comment_user_alter_contributor_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='issue',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='softdesk.issue'),
        ),
        migrations.AlterField(
            model_name='contributor',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='softdesk.project'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='assigned_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='issues_assigned', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='issue',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='issues', to='softdesk.project'),
        ),
    ]
