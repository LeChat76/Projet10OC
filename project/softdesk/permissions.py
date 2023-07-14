from rest_framework.permissions import BasePermission

from .models import Contributor, Project, Issue


# class IsAdmin(BasePermission):

#     def has_permission(self, request, view):
#         # LIST, CREATE
#         print('REQUEST', request.user)
#         return super().has_permission(request, view)
    
    
#     def has_object_permission(self, request, view, obj):
#         # PATCH, PUT, UPDATE, DELETE
#         print('REQUEST', request.user)
#         print('OBJ', obj)
#         return super().has_object_permission(request, view, obj)
    
class IsIssueAuthorized(BasePermission):
    # test if user is authorized to create issue for specific project :
    def has_permission(self, request, view):
        project_id = request.data.get('project')
        print('PROJECT', project_id)
        print('USERNAME', request.user)
        return bool(
            # check if "couple user-project" exist in contributor table
            Contributor.objects.filter(project_id=project_id, user=request.user).exists() or 
            # check if user is author of the project
            Project.objects.filter(id=project_id, user=request.user).exists()
        )

class IsCommentAuthorized(BasePermission):
    # test if user is authorized to create issue for specific project :
    def has_permission(self, request, view):
        issue_id = request.data.get('issue')
        print('ISSUE', issue_id)
        print('USERNAME', request.user)
        # test if issue_id is associated to an issue in the table
        if Issue.objects.filter(id=issue_id).exists():
            # if YES, collect project_id associated to the issue
            project_id = Issue.objects.filter(id=issue_id).values('project').first().get('project')
            print('PROJECT_ID', project_id)
            return bool(
                # check if "couple user-project" exist in contributor table
                Contributor.objects.filter(project_id=project_id, user=request.user).exists() or 
                # check if user is author of the project
                Project.objects.filter(id=project_id, user=request.user).exists()
            )
        return False
