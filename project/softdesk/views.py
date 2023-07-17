from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import Contributor, Project, Issue, Comment
from .serializers import ContributorSerializer, ProjectSerializer, IssueSerializer, CommentSerializer
from .permissions import IsIssueAuthorized, isContributorAuthorized, IsProjectAuthorized, IsCommentAuthorized


class ContributorViewset(ModelViewSet):

    permission_classes = [IsAuthenticated, isContributorAuthorized]
    serializer_class = ContributorSerializer

    def get_queryset(self):
        user = self.request.user
        return Contributor.objects.filter(user=user)
    
    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     user = request.user
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     project_title = serializer.data['title']
    #     message = f"Projet '{project_title}' créé par {user.username}."
    #     return Response(message, status=status.HTTP_201_CREATED, headers=headers)

class ProjectViewset(ModelViewSet):
     
    permission_classes = [IsAuthenticated, IsProjectAuthorized]
    serializer_class = ProjectSerializer

    def get_queryset(self):
        # for container in self.__dict__:
        #     print('SELF:', container)
        return Project.objects.filter(user=self.request.user)

    # def perform_create(self, serialized_data):
    #     # function overloaded to add a record in contributor table automaticaly when create a new project
    #     project = serialized_data.save()
    #     Contributor.objects.create(project=project, user=self.request.user)

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     user = request.user
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     project_title = serializer.data['title']
    #     message = f"Projet '{project_title}' créé par {user.username}."
    #     return Response(message, status=status.HTTP_201_CREATED, headers=headers)
    
    # def destroy(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     self.perform_destroy(instance)
    #     message=f'Projet {instance.title} supprimé.'
    #     return Response(message, status=status.HTTP_204_NO_CONTENT)
    
class IssueViewset(ModelViewSet):

    permission_classes = [IsAuthenticated, IsIssueAuthorized]
    serializer_class = IssueSerializer

    def get_queryset(self):
        # display only issue associated to this user
        return Issue.objects.filter(user=self.request.user)
    
class CommentViewset(ModelViewSet):
    
    permission_classes = [IsAuthenticated, IsCommentAuthorized]
    serializer_class = CommentSerializer

    def get_queryset(self):
        # display only comment associated to this user
        return Comment.objects.filter(user=self.request.user)
    