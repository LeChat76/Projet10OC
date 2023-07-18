from rest_framework.permissions import BasePermission

from .models import Contributor, Project, Issue, Comment

class IsProjectAuthorized(BasePermission):

    # check is current user is authorized to delete project
    def has_object_permission(self, request, view, obj):
        project_id = obj.id
        user = request.user
        print('PROJECT_AUTHOR', project_id)
        print('USER', user)
        return bool(Project.objects.filter(id=project_id, user=user).exists() or 
                    Contributor.objects.filter(project_id=project_id, user=user).exists()
        )

class isContributorAuthorized(BasePermission):

    # check if current user is authorized to add contributor
    def has_permission(self, request, view):
        project_id = request.data.get('project')
        project_author = Project.objects.filter(id=project_id).values('user').first()['user']
        current_user = request.user
        user = request.data.get('user')
        print('PROJECT_ID', project_id)
        print('PROJECT_AUTHOR', project_author)
        print('CURRENT_USER.id', current_user.id)
        print('USER', user)
        return bool(
            Project.objects.filter(id=project_id, user=current_user).exists() and 
            (int(user) != int(current_user.id))
        )
        
class IsIssueAuthorized(BasePermission):

    # check if connected user is authorized to add Issue
    def has_permission(self, request, view):
        project_id = request.data.get('project')
        user = request.user
        print('PROJECT', project_id)
        print('USERNAME', user)
        return bool(
            # check if "couple user-project" exist in contributor table
            Contributor.objects.filter(project_id=project_id, user=user).exists() or 
            # check if user is author of the project
            Project.objects.filter(id=project_id, user=request.user).exists()
        )
    
    def has_object_permission(self, request, view, obj):
        return bool(
            # check if logged user is the author of the comment
            Issue.objects.filter(user=request.user).exists()
        )

class IsCommentAuthorized(BasePermission):

    def has_permission(self, request, view):
        if request.method in ['GET', 'POST']:
            print('HAS_PERM')
        # user = request.user
        # issue_id = request.data.get('issue')
        # project_id = Issue.objects.filter(id=issue_id).firstprint('')
        # return bool(
        #     # check if user is contributor
        #     Contributor.objects.filter(project=project_id, user=user).exists() or 
        #     # otherwise if user is project's author
        #     Project.objects.filter(user=request.user).exists()
        # )
        return True

    def has_object_permission(self, request, view, obj):
        print('HAS_OBJ')
        # return bool(
        #     # check if logged user is the author of the comment
        #     Comment.objects.filter(user=request.user).exists()
        # )
