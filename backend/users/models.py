from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    company_name = models.CharField(max_length=1024)
    vat_id = models.CharField(max_length=255)
    address = models.TextField()
