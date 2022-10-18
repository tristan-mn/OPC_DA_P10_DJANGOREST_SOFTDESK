"""softdesk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework_nested import routers
from rest_framework_simplejwt.views import TokenObtainPairView

from authentication.views import UserViewset, SignupView
from app.views import ProjectsViewset, ManageUsersProjectViewset, IssuesViewset, CommentsViewset

router = routers.SimpleRouter()
router.register('users', UserViewset, basename='user')
router.register('projects', ProjectsViewset, basename="projects")

projects_router = routers.NestedSimpleRouter(router, 'projects', lookup='project')
projects_router.register('users', ManageUsersProjectViewset, basename="manage_users_project")
projects_router.register('issues', IssuesViewset, basename="issues")

issues_router = routers.NestedSimpleRouter(projects_router, 'issues', lookup='issue')
issues_router.register('comments', CommentsViewset, basename="comments")

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('api/', include(projects_router.urls)),
    path('api', include(issues_router.urls)),
    path('api/signup/', SignupView.as_view(), name='signup'),
    path('api/login/', TokenObtainPairView.as_view(), name='login'),
]
