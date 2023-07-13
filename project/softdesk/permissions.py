from rest_framework.permissions import BasePermission
from rest_framework import permissions
from .models import Contributor, Project

class IsAdmin(BasePermission):

    def has_permission(self, request, view):
        # LIST, CREATE
        print('REQUEST', request.user)
        return super().has_permission(request, view)
    
    
#     def has_object_permission(self, request, view, obj):
#         # PATCH, PUT, UPDATE, DELETE
#         print('REQUEST', request.user)
#         print('OBJ', obj)
#         return super().has_object_permission(request, view, obj)
    
class IsAuthorized(permissions.BasePermission):

    def has_obj_permission(self, request, view):
        # For PATCH, PUT, UPDATE, DELETE
        project_id = request.data.get('project')
        if project_id is None:
            return False
        is_contributor = Contributor.objects.filter(project_id=project_id, user=request.user).exists()
        if is_contributor:
            return True
        is_author = Project.objects.filter(id=project_id, user=request.user).exists()
        if is_author:
            return True    
        else:
            return False
    
    def has_permission(self, request, view, obj):
        # For LIST, CREATE
        project_id = request.data.get('project')
        if Project.objects.filter(id=project_id, user=request.user).exists():
            return True
        else:
            return False
