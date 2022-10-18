from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from app.models import Project, Contributor, Issue, Comment
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

class IssueListSerializer(ModelSerializer):

    class Meta:
        model = Issue
        fields = ['title', 'desc', 'tag', 'priority', 'status']


class IssueDetailSerializer(ModelSerializer):
    author = UserListSerializer()
    assignee = UserListSerializer()
    class Meta:
        model = Issue
        fields = ['title', 'project', 'created_time', 'desc', 'tag', 'priority', 'status', 'author', 'assignee']

class CommentListSerializer(ModelSerializer):

    class Meta:
        model = Comment
        fields = ['description']


class CommentDetailSerializer(ModelSerializer):
    author = UserListSerializer()
    issue = IssueListSerializer()
    class Meta:
        model = Issue
        fields = ['description', 'author', 'issue', 'created_time']
