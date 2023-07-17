from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from softdesk.models import Contributor, Project, Issue, Comment
 
class ProjectSerializer(ModelSerializer):

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Project
        fields = [
            'user',
            'id',
            'type',
            'title',
            'description',
        ]

class ContributorSerializer(ModelSerializer):
 
    class Meta:
        model = Contributor
        fields = [
            'project',
            'user',
        ]

class IssueSerializer(ModelSerializer):

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = Issue
        fields = [
            'title',
            'description',
            'type',
            'priority',
            'statut',
            'user',
            'project',
        ]

class CommentSerializer(ModelSerializer):

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Comment
        fields = [
            'user',
            'id',
            'issue',
            'description',
        ]