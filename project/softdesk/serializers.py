from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from softdesk.models import Contributor, Project, Issue, Comment


class ProjectListSerializer(ModelSerializer):

    class Meta:
        model = Project
        fields = [
            'id',
            'title',
        ]

class ProjectDetailSerializer(ModelSerializer):
    
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Project
        fields = [
            'id',
            'user',
            'type',
            'title',
            'description',
        ]

class ContributorSerializer(ModelSerializer):
 
    class Meta:
        model = Contributor
        fields = [
            'id',
            'project',
            'user',
        ]

class IssueListSerializer(ModelSerializer):

    class Meta:
        model = Issue
        fields = [
            'id',
            'title',
        ]

class IssueDetailSerializer(ModelSerializer):

    user = serializers.PrimaryKeyRelatedField(default=serializers.CurrentUserDefault(), many=False, read_only=False)

    class Meta:
        model = Issue
        fields = [
            'id',
            'title',
            'description',
            'type',
            'priority',
            'statut',
            'user',
            'project',
        ]

class CommentListSerializer(ModelSerializer):

    class Meta:
        model = Comment
        fields = [
            'id',
            'description',
        ]

class CommentDetailSerializer(ModelSerializer):

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Comment
        fields = [
            'id',
            'user',
            'issue',
            'description',
        ]