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
        fields = '__all__'

class ContributorSerializer(ModelSerializer):

    class Meta:
        model = Contributor
        fields = '__all__'

class IssueListSerializer(ModelSerializer):

    # user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Issue
        fields = [
            'id',
            'title',
        ]

class IssueDetailSerializer(ModelSerializer):

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    def create(self, validated_data):
        assigned_user = validated_data.get('assigned_user')
        if not assigned_user:
            validated_data['assigned_user'] = self.context['request'].user
        instance = Issue.objects.create(**validated_data)
        return instance

    class Meta:
        model = Issue
        fields = '__all__'

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
        fields = '__all__'