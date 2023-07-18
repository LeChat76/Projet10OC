from rest_framework.permissions import BasePermission

from .models import Contributor, Project, Issue, Comment

class IsProjectAuthorized(BasePermission):

    def has_object_permission(self, request, view, obj):
        project_id = obj.id
        user = request.user
        print('PROJECT_AUTHOR', project_id)
        print('USER', user)
        return bool(Project.objects.filter(id=project_id, user=user).exists() or 
                    Contributor.objects.filter(project_id=project_id, user=user).exists()
        )

class isContributorAuthorized(BasePermission):

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

    def has_permission(self, request, view):
        if request.method == 'POST':
            user=request.user
            project_id = request.data.get('project')
            # print('PROJECT_ID', project_id)
            if Project.objects.filter(id=project_id).exists():
                return bool(
                    # check if authenticated user is contributor of this project
                    Contributor.objects.filter(project_id=project_id, user=user).exists() or 
                    # otherwise if authenticated user is project's author
                    Project.objects.filter(id=project_id, user=request.user).exists()
            )

        return True

    
    def has_object_permission(self, request, view, obj):
        if request.method in ['DELETE', 'GET']:
            user = request.user
            project_id = obj.project.id
            print('PROJECT_ID', project_id)
            return bool(
                # check if authenticated user is contributor of this project
                Contributor.objects.filter(project=project_id, user=user).exists() or 
                # otherwise if authenticated user is project's author
                Project.objects.filter(id=project_id, user=user).exists()
            )

class IsCommentAuthorized(BasePermission):

    def has_permission(self, request, view):
        if request.method == 'POST':
            user=request.user
            issue_id = request.data.get('issue')
            # print('ISSUE_ID', issue_id)
            if Issue.objects.filter(id=issue_id).exists():
                project_id = Issue.objects.filter(id=issue_id).values('project').first()['project']
                # print('PROJECT_ID', project_id)
                # print('POST_METHOD')
                return bool(
                    # check if authenticated user is contributor of this project
                    Contributor.objects.filter(project=project_id, user=user).exists() or 
                    # otherwise if authenticated user is project's author
                    Project.objects.filter(id=project_id, user=user).exists()
                )

        return True
    
    def has_object_permission(self, request, view, obj):
        if request.method in ['DELETE', 'GET']:
            user = request.user
            # print('USER', user)
            issue_id = obj.issue.id
            # print('ISSUE_ID', issue_id)
            project_id = Issue.objects.filter(id=issue_id).values('project').first()['project']
            # print('PROJECT_ID', project_id)
            return bool(
                # check if authenticated user is contributor of this project
                Contributor.objects.filter(project=project_id, user=user).exists() or 
                # otherwise if authenticated user is project's author
                Project.objects.filter(id=project_id, user=user).exists()
            )
        