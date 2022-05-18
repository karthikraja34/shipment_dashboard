from django.contrib.auth.models import AbstractUser
from django.db import models
from model_utils.models import TimeStampedModel


class User(AbstractUser):
    company = models.ForeignKey("users.Company", on_delete=models.CASCADE, null=True)


class Company(TimeStampedModel):
    name = models.CharField(max_length=1025)
    address = models.TextField()
    vat_id = models.CharField(max_length=255)
