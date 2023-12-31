# Generated by Django 4.2.3 on 2023-07-06 15:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('softdesk', '0005_issues_alter_projects_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='issues',
            name='contributor',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='Issues', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='issues',
            name='project',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='Issues', to='softdesk.projects'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contributors',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Contributors', to='softdesk.projects'),
        ),
        migrations.AlterField(
            model_name='contributors',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Contributors', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='projects',
            name='contributor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Projects', to=settings.AUTH_USER_MODEL),
        ),
    ]
