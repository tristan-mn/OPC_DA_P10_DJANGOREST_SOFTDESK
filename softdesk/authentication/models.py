from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField( unique=True, blank=False)
    password = models.CharField(max_length=64)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [first_name, last_name, password]