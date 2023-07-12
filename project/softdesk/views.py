from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .models import Contributor, Project, Issue, Comment
from .serializers import ContributorSerializer, ProjectSerializer, IssueSerializer, CommentSerializer
from .permissions import IsAdmin

class ContributorViewset(ModelViewSet):

    permission_classes = [IsAuthenticated]
    serializer_class = ContributorSerializer

    def get_queryset(self):
        user = self.request.user
        return Contributor.objects.filter(user=user)

class ProjectViewset(ModelViewSet):
     
    permission_classes = [IsAuthenticated]
    serializer_class = ProjectSerializer

    def get_queryset(self):
        user = self.request.user
        return Project.objects.filter(user=user)

    def perform_create(self, serializer):
        # function overloaded to add a record in contributor table
        # automaticaly when create a new project
        project = serializer.save()
        user = self.request.user
        Contributor.objects.create(project=project, user=user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = request.user
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        project_title = serializer.data['title']
        message = f"Projet '{project_title}' créé par {user.username}."
        return Response(message, status=status.HTTP_201_CREATED, headers=headers)
    
    def destroy(self, request, *args, **kwargs):
        # not necessary, just to have a 'beautifull' report when delete project ;-)
        instance = self.get_object()
        self.perform_destroy(instance)
        message=f'Projet {instance.title} supprimé.'
        return Response(message, status=status.HTTP_204_NO_CONTENT)
    
class IssueViewset(ModelViewSet):

    serializer_class = IssueSerializer

    def get_queryset(self):
        return Issue.objects.all()

class CommentViewset(ModelViewSet):

    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.all()
    