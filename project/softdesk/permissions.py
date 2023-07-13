from rest_framework.permissions import BasePermission
from rest_framework import permissions
from .models import Contributor, Project

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
    
class IsContributor(permissions.BasePermission):
    def has_permission(self, request, view):
        project_id = request.data.get('project')
        contributor = Contributor.objects.filter(project_id=project_id, user=request.user).exists()
        return contributor

class IsAuthor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        project_id = request.data.get('project')
        author = Project.objects.filter(project_id=project_id, user=request.user).exists()
        return author

