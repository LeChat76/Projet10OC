from django.shortcuts import render
from rest_framework import status

from rest_framework.viewsets import ModelViewSet
from .models import Users
from .serializers import UserSerializer
from django.contrib.auth.hashers import make_password

class UserViewset(ModelViewSet):

    serializer_class = UserSerializer
    queryset = Users.objects.filter(is_superuser='0')

    # def update(self, request):
    #     password = make_password(request['password'])  # enhances password hashing
    #     user = Users(**request)
    #     user.set_password(password) # password hashing
    #     user.save()
    #     return user

