from rest_framework import status
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from .models import Users
from .serializers import UserSerializer


class UserViewset(ModelViewSet):

    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer

    def get_queryset(self):
        return Users.objects.filter(is_superuser='0')
    
    # def create(self, request, *args, **kwargs):
    #     # not necessary, just to have a 'beautifull' report when creating user ;-)
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     username = serializer.data['username']
    #     message = f'Utilisateur {username} créé.'
    #     return Response(message, status=status.HTTP_201_CREATED, headers=headers)

    # def destroy(self, request, *args, **kwargs):
    #     # not necessary, just to have a 'beautifull' report when delete user ;-)
    #     instance = self.get_object()
    #     self.perform_destroy(instance)
    #     message=f'Utilisateur {instance.username} supprimé.'
    #     return Response(message, status=status.HTTP_204_NO_CONTENT)
    

