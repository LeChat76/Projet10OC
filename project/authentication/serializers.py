from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from datetime import date
from .constantes import MIN_AGE

from authentication.models import Users
 
class UserSerializer(ModelSerializer):
 
    MIN_AGE = 15

    password = serializers.CharField(write_only=True)
    birthday = serializers.DateField(format='%d-%m-%Y')

    class Meta:
        model = Users
        fields = [
            'id',
            'username',
            'birthday',
            'password',
            'can_be_contacted',
            'can_data_be_shared',
        ]
    
    def validate_birthday(self, value):
        today = date.today()
        age = today.year - value.year - ((today.month, today.day) < (value.month, value.day))
        if age < MIN_AGE:
            raise serializers.ValidationError("Vous devez avoir au moins 15 ans pour créer un compte.")
        return value

    def create(self, validated_data):
        user = Users(**validated_data)
        user.set_password(user.password) # password hashing
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.username = validated_data['username']
        instance.set_password(validated_data['password'])
        instance.birthday = validated_data['birthday']
        instance.save()
        return instance