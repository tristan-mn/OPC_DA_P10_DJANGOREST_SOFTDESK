from rest_framework.permissions import BasePermission, SAFE_METHODS
from app.models import Project, Contributor

class ProjectPermissions(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user


class ContributorPermission(BasePermission):
    
    def has_permission(self, request, view):
        project = Project.objects.get(id=view.kwargs['project_pk'])
        if request.method in SAFE_METHODS:
            return True
        return request.user == project.author
    
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user

class IssueCommentPermissions(BasePermission):

    def has_permission(self, request, view):
        return Contributor.objects.filter(project=view.kwargs['project_pk'], user=request.user).exists()

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author== request.user
