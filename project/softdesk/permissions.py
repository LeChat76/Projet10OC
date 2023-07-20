from rest_framework.permissions import BasePermission

from .models import Contributor, Project, Issue, Comment

class IsProjectAuthorized(BasePermission):
    
    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        user = request.user
        # print('USER', user)
        project_id = obj.id
        # print('PROJECT_ID', project_id)
        if request.method == 'GET':
            return bool(
                Project.objects.filter(id=project_id, user=user).exists() or 
                Contributor.objects.filter(user=user, project=project_id)
            )
        elif request.method in ['PATCH', 'DELETE']:
            return bool(Project.objects.filter(id=project_id, user=user).exists())

class isContributorAuthorized(BasePermission):

    def has_permission(self, request, view):
        if request.method == 'POST':
            project_id = request.data.get('project')
            current_user = request.user
            user_to_add = request.data.get('user')
            return bool(
                Project.objects.filter(id=project_id, user=current_user).exists() and 
                (int(user_to_add) != int(current_user.id))
            )
        
        return True

    def has_object_permission(self, request, view, obj):
        user = request.user
        contributor_id = view.kwargs['pk']
        projects = Project.objects.filter(user=user)
        if request.method == 'DELETE':
            print('TOP')
            return bool(Contributor.objects.filter(project__in=projects).exists())
        
class IsIssueAuthorized(BasePermission):

    def has_permission(self, request, view):
        if request.method == 'POST':
            user=request.user
            project_id = request.data.get('project')
            if Project.objects.filter(id=project_id).exists():
                return bool(
                    # check if authenticated user is contributor of this project
                    Contributor.objects.filter(project_id=project_id, user=user).exists() or 
                    # otherwise if authenticated user is project's author
                    Project.objects.filter(id=project_id, user=request.user).exists()
            )

        return True

    def has_object_permission(self, request, view, obj):
        user = request.user
        project_id = obj.project.id
        if request.method in ['GET', 'PATCH']:
            return bool(
                # check if authenticated user is contributor of this project
                Contributor.objects.filter(project=project_id, user=user).exists() or 
                # otherwise if authenticated user is project's author
                Project.objects.filter(id=project_id, user=user).exists()
            )
        elif request.method == 'DELETE':
            issue_id = view.kwargs['pk']
            return bool(Issue.objects.filter(user=user, id=issue_id).exists())

class IsCommentAuthorized(BasePermission):

    def has_permission(self, request, view):
        if request.method in ['POST', 'GET']:
            user=request.user
            # print('USER_PERM', user)
            issue_id = request.data.get('issue')
            # print('ISSUE_ID_PERM', issue_id)
            if Issue.objects.filter(id=issue_id).exists():
                project_id = Issue.objects.filter(id=issue_id).values('project').first()['project']
                # print('PROJECT_ID_PERM', project_id)
                return bool(
                    # check if authenticated user is contributor of this project
                    Contributor.objects.filter(project=project_id, user=user).exists() or 
                    # otherwise if authenticated user is project's author
                    Project.objects.filter(id=project_id, user=user).exists()
                )
        return True
    
    def has_object_permission(self, request, view, obj):
        user = request.user
        # print('USER_OBJ_PERM', user)
        issue_id = obj.issue.id
        # print('ISSUE_ID_OBJ_PERM', issue_id)
        project_id = Issue.objects.filter(id=issue_id).values('project').first()['project']
        # print('PROJECT_ID_OBJ_PERM', project_id)
        if request.method in ['GET', 'PATCH']:
            return bool(
                # check if authenticated user is contributor of this project
                Contributor.objects.filter(project=project_id, user=user).exists() or 
                # otherwise if authenticated user is project's author
                Project.objects.filter(id=project_id, user=user).exists()
            )
        elif request.method == 'DELETE':
            return bool(Comment.objects.filter(user=user, issue=issue_id).exists())

class IsProjectIssueCommentAuthorized(BasePermission):
    
    def has_permission(self, request, view):
        user=request.user
        project_id = view.kwargs['project_pk']
        return bool(
            # check if authenticated user is contributor of this project
            Contributor.objects.filter(project=project_id, user=user).exists() or 
            # otherwise if authenticated user is project's author
            Project.objects.filter(id=project_id, user=user).exists()
        )
    