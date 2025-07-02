from django.contrib import admin
from .models import DeployedApp, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "username"]
    search_fields = ["id", "username"]
    list_filter = ()


@admin.register(DeployedApp)
class DeployedAppAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "user"]
    search_fields = ["id", "name", "user"]
    list_filter = ()
