from django.contrib import admin

# Register your models here.
from .models import Task
# Register your models here.

class TasksAdmin(admin.ModelAdmin):
    list_display = ("id", "taskName", "dueDate", "createDatetime", "updateDatetime", "completedDatetime", "taskOwnerId" )
    list_display_links = ("id", "taskName", "taskOwnerId" )

admin.site.register(Task, TasksAdmin)
