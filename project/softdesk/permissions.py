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
        user = request.user.id
        print('USER', user)
        project_id = obj.project_id
        print('PROJECT_ID', project_id)
        if request.method == 'DELETE':
            if Project.objects.filter(user=user, id=project_id):
                return True

class isProjectContributorAuthorized(BasePermission):

    def has_permission(self, request, view):
        if request.method == 'GET':
            user = request.user
            project_id = view.kwargs['project_pk']
            print('PROJECT_ID', project_id)
            if Project.objects.filter(user=user, id=project_id):
                return True

class IsIssueAuthorized(BasePermission):

    def has_permission(self, request, view):
        if request.method == 'POST':
            user=request.user
            assigned_user_id = request.data.get('assigned_user')
            if not assigned_user_id:
                assigned_user_id = user
            else:
                user = assigned_user_id
            project_id = request.data.get('project')
            print('USER', user)
            if Project.objects.filter(user=request.user, id=project_id) or Contributor.objects.filter(project_id=project_id, user=user):
                return bool(
                    # check if authenticated user is contributor of this project
                    Contributor.objects.filter(project_id=project_id, user=user).exists() or 
                    # otherwise if authenticated user is project's author
                    Project.objects.filter(id=project_id, user=user).exists()
                )
            else:
                return False
        return True

    def has_object_permission(self, request, view, obj):
        user = request.user
        project_id = obj.project.id
        if request.method in ['GET']:
            return bool(
                # check if authenticated user is contributor of this project
                Contributor.objects.filter(project=project_id, user=user).exists() or 
                # otherwise if authenticated user is project's author
                Project.objects.filter(id=project_id, user=user).exists()
            )
        elif request.method in ['DELETE']:
            issue_id = obj.id
            return bool(Issue.objects.filter(user=user, id=issue_id))
        
        elif request.method in ['PATCH']:
            issue_id = obj.id
            # only assigned user can just modify statut field of an issue
            if Issue.objects.filter(assigned_user=user, id=issue_id):
                 return True
            else:
                return False
            
class IsCommentAuthorized(BasePermission):

    def has_permission(self, request, view):
        if request.method in ['POST', 'GET']:
            user=request.user
            # print('USER_PERM', user)
            issue_id = request.data.get('issue')
            # print('ISSUE_ID_PERM', issue_id)
            if Issue.objects.filter(id=issue_id):
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
        # print('USER', user.id)
        issue_id = obj.id
        # print('ISSUE_ID', issue_id)
        if request.method in ['GET', 'PATCH']:
            return bool(Comment.objects.filter(user=user, id=issue_id))

        elif request.method == 'DELETE':
            return bool(Comment.objects.filter(user=user, id=issue_id))

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
    