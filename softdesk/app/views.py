from django.shortcuts import render

from rest_framework.exceptions import ValidationError
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from app.serializer import ProjectDetailSerializer, ProjectListSerializer, ContributorListSerializer, ContributorDetailSerializer, IssueListSerializer, IssueDetailSerializer, CommentListSerializer, CommentDetailSerializer
from app.models import Project, Contributor, Issue, Comment
# Create your views here.

class ProjectsViewset(ModelViewSet):

    queryset = Project.objects.all()
    serializer_class = ProjectDetailSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Project.objects.filter(contributor__user=self.request.user).order_by('id')


    def create(self, request, *args, **kwargs):
        serializer = ProjectListSerializer(data=request.data)
        serializer.is_valid()
        project = serializer.save(author=request.user)
        Contributor.objects.create(user=request.user, project=project, role='AUTHOR')
        return Response(serializer.data)
    

    def get_serializer_class(self):
        return super().get_serializer_class()

class ManageUsersProjectViewset(ModelViewSet):

    permission_classes = [IsAuthenticated]
    serializer_class = ContributorListSerializer
    detail_serializer_class = ContributorDetailSerializer

    def get_queryset(self):
        return Contributor.objects.filter(project=self.kwargs['project_pk'])


    def create(self, request, *args, **kwargs):
        serializer = ContributorListSerializer(data=request.data)
        serializer.is_valid()  
        serializer.save(project=Project.objects.get(pk=self.kwargs['project_pk']), id=request.data['user'])
        return Response(serializer.data)


    def get_serializer_class(self):
        if self.action == "retrieve":
            return self.detail_serializer_class
        return super().get_serializer_class()


class IssuesViewset(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = IssueListSerializer
    detail_serializer_class = IssueDetailSerializer

    def get_queryset(self):
        return Issue.objects.filter(project=self.kwargs['project_pk'])
    

    def create(self, request, *args, **kwargs):
        serializer = IssueListSerializer(data=request.data)
        serializer.is_valid()
        serializer.save(project=Project.objects.get(pk=self.kwargs['project_pk']), author=request.user, assignee=request.user)
        return Response(serializer.data)


    def get_serializer_class(self):
        if self.action == "retrieve":
            return self.detail_serializer_class
        return super().get_serializer_class()


class CommentsViewset(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CommentListSerializer
    detail_serializer_class = CommentDetailSerializer

    def get_query_set(self):
        return Comment.objects.filter(issue=self.kwargs['issue_pk'])
    

    def create(self, request, *args, **kwargs):
        serializer = CommentListSerializer(data=request.data)
        serializer.is_valid()
        serializer.save(issue=Issue.objects.get(pk=self.kwargs['issue_pk']), author=request.user)
        return Response(serializer.data)


    def get_serializer_class(self):
        if self.action == "retrieve":
            return self.detail_serializer_class
        return super().get_serializer_class()