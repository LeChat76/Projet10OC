from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from authentication.models import Users

from softdesk.models import Contributor, Project, Issue, Comment
 
class ContributorSerializer(ModelSerializer):
 
    class Meta:
        model = Contributor
        fields = [
            'project',
            'user',
        ]

class ProjectSerializer(ModelSerializer):

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Project
        fields = [
            'type',
            'title',
            'description',
            'user',
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