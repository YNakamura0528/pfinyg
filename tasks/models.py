from django.contrib.auth.models import User
from django.core import validators
from django.db import models

# Create your models here.
class Task(models.Model):
    taskName = models.CharField(max_length = 150, blank = False)
    taskImportance = models.IntegerField(default = 3,
                                         blank = False,
                                         validators = [
                                            validators.MinValueValidator(1),
                                            validators.MaxValueValidator(5)
                                            ])
    dueDate = models.DateField(blank = True, null = True)
    doneDate = models.DateField(blank = True, null = True)
    comment = models.CharField(max_length = 1024, blank = True, null = True)
    createDatetime = models.DateTimeField(auto_now_add=True)
    updateDatetime = models.DateTimeField(auto_now = True)
    completedDatetime = models.DateTimeField(blank = True, null = True)
    taskOwnerId = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "tasks")

    def __str__(self):
        return self.taskName
