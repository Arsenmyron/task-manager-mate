from django.contrib.auth.models import AbstractUser
from django.db import models


class TaskType(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Task(models.Model):
    PRIORITY_CHOICES = [
        ("LOW", "Low priority task"),
        ("MEDIUM", "Medium priority task"),
        ("HIGH", "High priority task"),
        ("URGENT", "Task with urgent priority"),
    ]
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    deadline = models.DateTimeField(blank=True, null=True)
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(max_length=8, choices=PRIORITY_CHOICES, null=True)
    task_type = models.ForeignKey(TaskType, on_delete=models.CASCADE, related_name="tasks")
    assignees = models.ManyToManyField("Worker", related_name="tasks")
    tags = models.ManyToManyField("Tag", related_name="tasks", blank=True)

    def __str__(self):
        return f"{self.name} ({self.priority})"


class Position(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Worker(AbstractUser):
    position = models.ForeignKey(Position, on_delete=models.CASCADE, related_name="workers", default=1)

    def __str__(self):
        return f"{self.position.name}: {self.first_name} {self.last_name} ({self.username})"

class Tag(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name