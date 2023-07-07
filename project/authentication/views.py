from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Users
from .serializers import UserSerializer

class UserViewset(ModelViewSet):

    serializer_class = UserSerializer

    def get_queryset(self):
        return Users.objects.all()