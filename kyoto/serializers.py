from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # Vous pouvez choisir les champs que vous voulez exposer via l'API
        fields = ['id', 'email', 'first_name', 'last_name', 'date_joined', 'is_active', 'is_admin']

class UserRegistrationSerializer(serializers.ModelSerializer):
    firstName = serializers.CharField(source='first_name')
    lastName = serializers.CharField(source='last_name')
    
    class Meta:
        model = User
        fields = ['lastName', 'firstName', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
