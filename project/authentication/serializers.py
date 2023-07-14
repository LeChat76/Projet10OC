from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from datetime import date

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
            raise serializers.ValidationError("Vous devez avoir au moins 15 ans pour créer un compte.")
        return value

    # def update(self, instance, validated_data):
    #     # overloaded def because password is stored in "clear format" so need to hash it
    #     instance.username = validated_data['username']
    #     instance.set_password(validated_data['password'])
    #     instance.birthday = validated_data['birthday']
    #     if validated_data['can_be_contacted']:
    #         instance.can_be_contacted = validated_data['can_be_contacted']
    #     if validated_data['can_data_be_shared']:
    #         instance.can_data_be_shared = validated_data['can_data_be_shared']
    #     instance.save()
    #     return instance
    
    # def partial_update(self, instance, validated_data):
    #     # overloaded method because password is stored in "clear format" so need to hash it
    #     print('DATA', validated_data)
    #     if validated_data['username']:
    #         instance.username = validated_data['username']
    #     if validated_data['password']:
    #         instance.set_password(validated_data['password'])
    #     if validated_data['birthday']:
    #         instance.birthday = validated_data['birthday']
    #     if validated_data['can_be_contacted']:
    #         instance.can_be_contacted = validated_data['can_be_contacted']
    #         print('SHARED', validated_data['can_data_be_shared'])
    #     if validated_data['can_data_be_shared']:
    #         instance.can_data_be_shared = validated_data['can_data_be_shared']
    #     instance.save()
    #     return instance