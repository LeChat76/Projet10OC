from django.contrib import admin

from softdesk.models import Project, Contributor, Issue, Comment

class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'type',
        'description',
        'project_contributor',
        'created_time'
    )

class ContributorAdmin(admin.ModelAdmin):
    list_display = (
        'contributor_user',
        'contributor_project',
    )

class IssuAdmin(admin.ModelAdmin):
    list_display = (
        'issue_project',
        'issue_contributor',
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
        'comment_user',
        'comment_issue',
    )

admin.site.register(Project, ProjectAdmin)
admin.site.register(Contributor, ContributorAdmin)
admin.site.register(Issue, IssuAdmin)
admin.site.register(Comment, CommentAdmin)
