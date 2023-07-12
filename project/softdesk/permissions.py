from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):

    def has_permission(self, request, view):
        # LIST, CREATE
        print('REQUEST', request.user)
        return super().has_permission(request, view)
    
    
    def has_object_permission(self, request, view, obj):
        # PATCH, PUT, UPDATE, DELETE
        print('REQUEST', request.user)
        print('OBJ', obj)
        return super().has_object_permission(request, view, obj)