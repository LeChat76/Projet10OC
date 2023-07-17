from rest_framework.permissions import BasePermission
from .models import Users

# class IsUserAuthorized(BasePermission):

    # def has_permission(self, request, view):
    #     # LIST, POST
    #     print('REQUEST', request.user)
    #     return super().has_permission(request, view)
    
    
    # def has_object_permission(self, request, view, obj):
        # PATCH, PUT, UPDATE, DELETE
        # print('REQUEST', request.data['username'])
        # print('OBJ', obj.username)
        #  if request.data['username'] == obj.username:
        #      return True
        # except:
        #     return False