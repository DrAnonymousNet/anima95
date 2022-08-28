from pyexpat import model
from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Post)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'slug', 'author')



