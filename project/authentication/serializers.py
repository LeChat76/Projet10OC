from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
 
from authentication.models import Users
 
class UserSerializer(ModelSerializer):
 
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Users
        fields = [
            'username',
            'password',
            'birthday',
            'can_be_contacted',
            'can_data_be_shared',
        ]
    
    def create(self, request):
        password = make_password(request['password'])  # enhances password hashing
        user = Users(**request)
        # user.birthday = serializers.DateField(format="%d-%m-%Y")
        user.set_password(password) # password hashing
        user.save()
        print('USER:', user.birthday)
        return user
