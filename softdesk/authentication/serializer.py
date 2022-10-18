from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from authentication.models import User

class UserDetailSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'password']

    def validate_name(self, value):
        if User.objects.filter(first_name=value).exists():
            raise serializers.ValidationError('User already exists')
        return value

class UserListSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name']

class SignupSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']
    
    def create(self, value):
        user = User.objects.create(username=value['email'],
                                   first_name=value['first_name'],
                                   last_name=value['last_name'],
                                   email=value['email'],
                                   )
        user.set_password(value['password'])
        user.save()
        return user
