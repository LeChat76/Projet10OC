from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from .models import Contributor, Project, Issue, Comment
from .serializers import ProjectListSerializer, ProjectDetailSerializer
from .serializers import ContributorSerializer
from .serializers import IssueListSerializer, IssueDetailSerializer
from .serializers import CommentListSerializer, CommentDetailSerializer
from .permissions import IsIssueAuthorized, isContributorAuthorized, IsCommentAuthorized, IsProjectIssueCommentAuthorized, IsProjectAuthorized


class ContributorViewset(ModelViewSet):

    permission_classes = [IsAuthenticated, isContributorAuthorized]
    serializer_class = ContributorSerializer

    def get_queryset(self):
        # display list of contributors of my projects
        user = self.request.user
        projects = Project.objects.filter(user=user)
        # print('PROJECT_ID', projects)
        return Contributor.objects.filter(project__in=projects)

class ProjectViewset(ModelViewSet):
     
    permission_classes = [IsAuthenticated ,IsProjectAuthorized]

    def get_queryset(self):
        user=self.request.user
        try:
            project_id = self.kwargs['pk']
        except:
            return Project.objects.filter(user=user)
        return Project.objects.filter(id=project_id)

    def get_serializer_class(self):
        if self.action == 'list':
            return ProjectListSerializer
        else:
            return ProjectDetailSerializer


class ProjectIssueViewset(ModelViewSet):

    permission_classes = [IsAuthenticated, IsProjectIssueCommentAuthorized]
    serializer_class = IssueDetailSerializer

    def get_queryset(self):
        # user = self.request.user
        project_id = self.kwargs['project_pk']
        issues_list = Issue.objects.filter(project=project_id)
        return issues_list
    
    def list(self, request, project_pk=None):
        issues = self.get_queryset()
        serializer = IssueListSerializer(issues, many=True)
        return Response(serializer.data)

class ProjectIssueCommentViewset(ModelViewSet):
    
    permission_classes = [IsAuthenticated, IsProjectIssueCommentAuthorized]
    serializer_class = CommentDetailSerializer

    def get_queryset(self):
        # user = self.request.user
        # print('USER_VIEW', user)
        project_id = self.kwargs['project_pk']
        # print('PROJECT_ID_VIEW', project_id)
        issue_id = self.kwargs['issue_pk']
        # print('ISSUE_ID_VIEW', issue_id)
        comment_list = []
        if Issue.objects.filter(id=issue_id, project=project_id):
            if Comment.objects.filter(issue=issue_id):
                # print('TOP2_VIEW')
                comment_list = Comment.objects.filter(issue=issue_id)
            # print('COMMENT_LIST_VIEW', comment_list)
        return comment_list

class IssueViewset(ModelViewSet):

    permission_classes = [IsAuthenticated, IsIssueAuthorized]

    def get_queryset(self):
        user = self.request.user
        # print('USER', user)
        try: 
            issue_id = self.kwargs['pk']
        except:
            return Issue.objects.filter(user=user)
        
        return Issue.objects.filter(id=issue_id)

    def create(self, request, project_pk=None, *args, **kwargs):
            data = request.data
            issue = Issue.objects.create(project=data['project'], title=data['title'], description=data['description'], priority=data['priority'], project_id=project_pk, status=data['statut'], user_id=request.user.id)
            issue.save()
            serializer = IssueDetailSerializer(issue)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


    
    def get_serializer_class(self):
        if self.action == 'list':
            return IssueListSerializer
        else:
            return IssueDetailSerializer

class CommentViewset(ModelViewSet):
    
    permission_classes = [IsAuthenticated, IsCommentAuthorized]

    def get_queryset(self):
        user=self.request.user
        try:
            comment_id = self.kwargs['pk']
            print('COMMENT_ID', comment_id)
        except:
            return Comment.objects.filter(user=user)

        return Comment.objects.filter(id=comment_id) 


    def get_serializer_class(self):
        if self.action == 'list':
            return CommentListSerializer
        else:
            return CommentDetailSerializer