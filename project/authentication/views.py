from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from .models import Users
from .serializers import UserDetailSerializer, UserListSerializer


class UserViewset(ModelViewSet):

    serializer_class = UserDetailSerializer

    def get_queryset(self):
        return Users.objects.filter(is_superuser='0')

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        # check if password is provided
        if 'password' not in serializer.validated_data:
            raise ValidationError("Le mot de passe est obligatoire.")

        self.perform_update(serializer)

        user_data = serializer.data

        return Response(user_data)
    
    def get_serializer_class(self):
        if self.action == 'list':
            return UserListSerializer
        else:
            return UserDetailSerializer