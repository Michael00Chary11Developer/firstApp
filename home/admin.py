from django.contrib import admin
from todo import models
# Register your models here.


@admin.register(models.Todo)
class TodoAdmin(admin.ModelAdmin):
    pass
