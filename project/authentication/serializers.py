from rest_framework.serializers import ModelSerializer
 
from authentication.models import Users
 
class UserSerializer(ModelSerializer):
 
    class Meta:
        model = Users
        fields = [
            'username',
        ]