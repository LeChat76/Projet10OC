from django.db import models, transaction
from django.conf import settings


class Project(models.Model):
    TYPES_PROJECT = (
        ('backend', 'Back-end'),
        ('frontend', 'Front-end'),
        ('ios', 'iOS'),
        ('android', 'Android')
    )
    type = models.CharField(max_length=10, choices=TYPES_PROJECT)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    project_contributor = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='Project_contributor',
    )
    created_time = models.DateTimeField(auto_now_add=True)


class Contributor(models.Model):
    contributor_user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='Contributor_user',
    )
    contributor_project = models.ForeignKey(
        to=Project,
        on_delete=models.CASCADE,
        related_name='Contributor_project',
    )

class Issue(models.Model):
    issue_project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='Issue_project',
    )
    issue_contributor = models.ForeignKey(
        Contributor,
        on_delete=models.CASCADE,
        related_name='Issue_contributor',
    )
    TYPES_PRIORITY = (
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    )
    priority = models.CharField(max_length=6, choices=TYPES_PRIORITY)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    TYPES_TYPE = (
        ('bug', 'Bug'),
        ('feature', 'Feature'),
        ('task', 'Task'),
    )
    type = models.CharField(max_length=7, choices=TYPES_TYPE)
    TYPES_STATUT = (
        ('todo', 'Todo'),
        ('inprogress', 'In progress'),
        ('finished', 'Finished'),
    )
    statut = models.CharField(default='todo', max_length=11, choices=TYPES_STATUT)
    created_time = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    description = models.CharField(max_length=500)
    comment_user = models.ForeignKey(
        Contributor,
        on_delete=models.CASCADE,
        related_name='Comment_user',
    )
    comment_issue = models.ForeignKey(
        Issue,
        on_delete=models.CASCADE,
        related_name='Comment_issue',
    )
    created_time = models.DateTimeField(auto_now_add=True)

