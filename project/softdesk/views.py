from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Contributor, Project, Issue, Comment
from .serializers import ContributorSerializer, ProjectSerializer, IssueSerializer, CommentSerializer

class ContributorViewset(ModelViewSet):

    serializer_class = ContributorSerializer

    def get_queryset(self):
        return Contributor.objects.all()

class ProjectViewset(ModelViewSet):
     
     serializer_class = ProjectSerializer

     def get_queryset(self):
         return Project.objects.all()
    
class IssueViewset(ModelViewSet):

    serializer_class = IssueSerializer

    def get_queryset(self):
        return Issue.objects.all()

class CommentViewset(ModelViewSet):

    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.all()
    