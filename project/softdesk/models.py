from django.db import models
from django.conf import settings
from django.utils import timezone
import uuid

class Project(models.Model):

    def __str__(self):
        return f'{self.title}'
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    TYPES_PROJECT = (
        ('backend', 'Back-end'),
        ('frontend', 'Front-end'),
        ('ios', 'iOS'),
        ('android', 'Android')
    )
    type = models.CharField(max_length=10, choices=TYPES_PROJECT)
    title = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=500, blank=True)
    created_time = models.DateTimeField(default=timezone.now)

class Contributor(models.Model):

    def __str__(self):
        return f'{self.project}'
    
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    project = models.ForeignKey(
        to=Project,
        on_delete=models.CASCADE,
    )
    created_time = models.DateTimeField(default=timezone.now)
    class Meta:
        unique_together = ('user', 'project')

class Issue(models.Model):

    def __str__(self):
        return f'{self.title}'
    
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='issues_author'
    )
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='issues'
    )
    assigned_user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='issues_assigned',
        null=True,
    )
    TYPES_PRIORITY = (
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    )
    TYPES_TYPE = (
        ('bug', 'Bug'),
        ('feature', 'Feature'),
        ('task', 'Task'),
    )
    TYPES_STATUT = (
        ('todo', 'Todo'),
        ('inprogress', 'In progress'),
        ('finished', 'Finished'),
    )
    priority = models.CharField(max_length=6, choices=TYPES_PRIORITY)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500, blank=True)
    type = models.CharField(max_length=7, choices=TYPES_TYPE)
    statut = models.CharField(default='todo', max_length=11, choices=TYPES_STATUT)
    created_time = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ('title', 'project')

class Comment(models.Model):
    description = models.CharField(max_length=500)
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    issue = models.ForeignKey(
        Issue,
        on_delete=models.CASCADE,
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_time = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ('user', 'description')