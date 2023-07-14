from rest_framework.viewsets import ModelViewSet
# from rest_framework.response import Response

from .models import Users
from .serializers import UserSerializer
from .permissions import IsUserAuthorized


class UserViewset(ModelViewSet):

    permission_classes = [IsUserAuthorized]
    serializer_class = UserSerializer

    def get_queryset(self):
        return Users.objects.filter(is_superuser='0')
