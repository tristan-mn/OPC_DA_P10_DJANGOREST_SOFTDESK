from random import choices
from django.db import models
from django.conf import settings
# Create your models here.


class Project(models.Model):
    BACKEND = "BACKEND"
    FRONTEND = "FRONTEND"
    ANDROID = "ANDROID"
    IOS = "IOS"

    TYPE_CHOICES = (
        (BACKEND, "Back-end"),
        (FRONTEND, "Front-end"),
        (ANDROID, "Android"),
        (IOS, "iOS"),
    )
    title = models.CharField(max_length=100)
    type = models.CharField(max_length=64, choices=TYPE_CHOICES)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="project_author")


class Contributor(models.Model):
    AUTHOR = "AUTHOR"
    CREATOR = "CREATOR"
    MANAGER = "MANAGER"
    ROLE_CHOICES = (
        (AUTHOR, 'auteur'),
        (CREATOR, 'créateur'),
        (MANAGER, 'responsable'),
    )

    contributor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="contributor")
    project = models.ForeignKey(Project ,on_delete=models.CASCADE)
    # à revoir
    # permission = models.Choices(value=True)
    role = models.CharField(max_length=30, choices=ROLE_CHOICES, verbose_name='Rôle')


class Issue(models.Model):
    LOW_PRIORITY = "LOW"
    MEDIUM_PRIORITY = "MEDIUM"
    HIGH_PRIORITY = "HIGH"
    PRIORITY_CHOICES = (
        (LOW_PRIORITY, "Faible"),
        (MEDIUM_PRIORITY, "Moyenne"),
        (HIGH_PRIORITY, "Élevée"),
    )

    BUG_TAG = "BUG"
    IMPROVEMENT_TAG = "IMPROVEMENT"
    TASK_TAG = "TASK"
    TAG_CHOICES = (
        (BUG_TAG, "Bug"),
        (IMPROVEMENT_TAG, "Amélioration"),
        (TASK_TAG, "Tâche"),
    )

    TODO_STATUS = "TODO"
    IN_PROGRESS_STATUS = "IN PROGRESS"
    COMPLETED_STATUS = "COMPLETED"
    STATUS_CHOICES = (
        (TODO_STATUS, "À faire"),
        (IN_PROGRESS_STATUS, "En cours"),
        (COMPLETED_STATUS, "Terminé"),
    )

    title = models.CharField(max_length=64)
    desc = models.CharField(max_length=300)
    tag = models.CharField(max_length=64, choices=TAG_CHOICES)
    priority = models.CharField(max_length=64, choices=PRIORITY_CHOICES)
    status = models.CharField(max_length=64, choices=STATUS_CHOICES)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="issue_author")
    assignee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="assignee")
    created_time = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    description = models.CharField(max_length=300)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comment_author")
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)