from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from app.models import Project, Contributor
from authentication.serializer import UserListSerializer

class ProjectListSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title', 'type']


class ProjectDetailSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title', 'type', 'author']


class ContributorListSerializer(ModelSerializer):
    project = ProjectDetailSerializer
    class Meta:
        model = Contributor
        fields = ['user', 'role']


class ContributorDetailSerializer(ModelSerializer):
    project = ProjectDetailSerializer
    user = UserListSerializer()
    class Meta:
        model = Contributor
        fields = ['user', 'role']
