from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .models import Contributor, Project, Issue, Comment
from .serializers import ContributorSerializer, ProjectSerializer, IssueSerializer, CommentSerializer
from .permissions import IsAdmin

class ContributorViewset(ModelViewSet):

    serializer_class = ContributorSerializer

    def get_queryset(self):
        return Contributor.objects.all()

class ProjectViewset(ModelViewSet):
     
    permission_classes = [IsAuthenticated]
    serializer_class = ProjectSerializer

    def get_queryset(self): # faire filtre pour afficher que les projet donc je suis contributeur et autheur
        return Project.objects.all()

    def create(self, request, *args, **kwargs):
        # not necessary, just to have a 'beautifull' report when created project associated to current user ;-)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = request.user
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        project_title = serializer.data['title']
        message = f'Projet {project_title} créé par {user.username}.'
        return Response(message, status=status.HTTP_201_CREATED, headers=headers)
    
class IssueViewset(ModelViewSet):

    serializer_class = IssueSerializer

    def get_queryset(self):
        return Issue.objects.all()

class CommentViewset(ModelViewSet):

    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.all()
    