from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import Contributor, Project, Issue, Comment
from .serializers import ContributorSerializer, ProjectSerializer, IssueSerializer, CommentSerializer
from .permissions import IsIssueAuthorized, isContributorAuthorized, IsProjectAuthorized, IsCommentAuthorized


class ContributorViewset(ModelViewSet):

    permission_classes = [IsAuthenticated, isContributorAuthorized]
    serializer_class = ContributorSerializer

    def get_queryset(self):
        # display only projet(s) I'm contributor
        user = self.request.user
        return Contributor.objects.filter(user=user)

class ProjectViewset(ModelViewSet):
     
    permission_classes = [IsAuthenticated, IsProjectAuthorized]
    serializer_class = ProjectSerializer

    def get_queryset(self):
        # display only project(s) associated to the authenticated user
        user=self.request.user
        return Project.objects.filter(user=user)
    
class IssueViewset(ModelViewSet):

    permission_classes = [IsAuthenticated, IsIssueAuthorized]
    serializer_class = IssueSerializer

    def get_queryset(self):
        # display only issue(s) associated to the authenticated user
        user=self.request.user
        return Issue.objects.filter(user=user)
    
class CommentViewset(ModelViewSet):
    
    permission_classes = [IsAuthenticated, IsCommentAuthorized]
    serializer_class = CommentSerializer

    def get_queryset(self):
        # display only comment(s) associated to the authenticated user
        user=self.request.user
        return Comment.objects.filter(user=user)
