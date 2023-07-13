from django.contrib import admin

from softdesk.models import Project, Contributor, Issue, Comment

class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'type',
        'description',
        'user',
        'created_time'
    )

class ContributorAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'project',
    )

class IssuAdmin(admin.ModelAdmin):
    list_display = (
        'project',
        'user',
        'priority',
        'title',
        'description',
        'type',
        'statut',
        'created_time',
    )

class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'description',
        'user',
        'issue',
    )

admin.site.register(Project, ProjectAdmin)
admin.site.register(Contributor, ContributorAdmin)
admin.site.register(Issue, IssuAdmin)
admin.site.register(Comment, CommentAdmin)
