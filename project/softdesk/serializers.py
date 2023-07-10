from rest_framework.serializers import ModelSerializer
 
from softdesk.models import Contributor, Project, Issue, Comment
 
class ContributorSerializer(ModelSerializer):
 
    class Meta:
        model = Contributor
        fields = [
            'contributor_project',
            'contributor_user',
        ]

class ProjectSerializer(ModelSerializer):

    class Meta:
        model = Project
        fields = [
            'type',
            'title',
            'description',
            'project_contributor',
        ]

class IssueSerializer(ModelSerializer):

    class Meta:
        model = Issue
        fields = [
            'title',
            'description',
            'type',
            'priority',
            'statut',
            'issue_contributor',
            'issue_project',
        ]

class CommentSerializer(ModelSerializer):

    class Meta:
        model = Comment
        fields = [
            'comment_issue',
            'comment_user',
            'description',
        ]