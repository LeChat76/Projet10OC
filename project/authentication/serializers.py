from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from datetime import date
from .models import hash_password

from .constantes import MIN_AGE
from authentication.models import Users


class UserSerializer(ModelSerializer):
 
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
            raise serializers.ValidationError(f'Vous devez avoir au moins {MIN_AGE} ans pour créer un compte.')
        return value
    