from django.db import models
from django.contrib.auth.models import AbstractUser
from project.settings import PLANS, PRO
from django.conf import settings


class User(AbstractUser):
    plan = models.IntegerField(choices=PLANS, default=PRO)

    groups = models.ManyToManyField(
        "auth.Group",
        verbose_name=("groups"),
        blank=True,
        related_name="user_set_for_app",
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        verbose_name=("user permissions"),
        blank=True,
        related_name="user_permissions_set",
        related_query_name="user",
    )

    def __str__(self):
        return self.username


class DeployedApp(models.Model):
    name = models.CharField(default="", max_length=250)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="app_user"
    )

    def __str__(self):
        return self.name
