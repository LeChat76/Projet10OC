from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import Contributor, Project, Issue, Comment
from .serializers import ProjectListSerializer, ProjectDetailSerializer
from .serializers import ContributorSerializer
from .serializers import IssueListSerializer, IssueDetailSerializer
from .serializers import CommentListSerializer, CommentDetailSerializer
from .permissions import IsIssueAuthorized, isContributorAuthorized, IsCommentAuthorized


class ContributorViewset(ModelViewSet):

    permission_classes = [IsAuthenticated, isContributorAuthorized]
    serializer_class = ContributorSerializer

    def get_queryset(self):
        # display only projet(s) I'm contributor
        user = self.request.user
        return Contributor.objects.filter(user=user)

class ProjectViewset(ModelViewSet):
     
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # display only project(s) associated to the authenticated user
        user=self.request.user
        return Project.objects.filter(user=user)

    def get_serializer_class(self):
        if self.action == 'list':
            return ProjectListSerializer
        else:
            return ProjectDetailSerializer


class IssueViewset(ModelViewSet):

    permission_classes = [IsAuthenticated, IsIssueAuthorized]

    def get_queryset(self):
        # display only issue(s) associated to the authenticated user
        user=self.request.user
        return Issue.objects.filter(user=user)
    
    def get_serializer_class(self):
        if self.action == 'list':
            return IssueListSerializer
        else:
            return IssueDetailSerializer
    
class CommentViewset(ModelViewSet):
    
    permission_classes = [IsAuthenticated, IsCommentAuthorized]

    def get_queryset(self):
        # display only comment(s) associated to the authenticated user
        user=self.request.user
        return Comment.objects.filter(user=user)

    def get_serializer_class(self):
        if self.action == 'list':
            return CommentListSerializer
        else:
            return CommentDetailSerializer