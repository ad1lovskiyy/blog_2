from django.contrib import admin
from . import models
from .models import About


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    search_fields = ("title",)
    ordering = ("created_at", "update_at")


@admin.register(models.Profile)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)
    ordering = ("created_at", "update_at")


@admin.register(models.Social_link)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name", )
    ordering = ("created_at", "update_at")


admin.site.register(About)