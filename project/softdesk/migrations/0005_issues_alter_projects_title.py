# Generated by Django 4.2.3 on 2023-07-06 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('softdesk', '0004_rename_project_id_contributors_project_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Issues',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proirity', models.CharField(choices=[('LOW', 'Low'), ('MEDIUM', 'Medium'), ('HIGH', 'High')], max_length=6)),
                ('title', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('BUG', 'Bug'), ('FEATURE', 'Feature'), ('TASK', 'Task')], max_length=7)),
                ('statut', models.CharField(choices=[('TODO', 'To do'), ('INPROGRESS', 'In progress'), ('FINISHED', 'Finished')], default='TODO', max_length=11)),
            ],
        ),
        migrations.AlterField(
            model_name='projects',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
