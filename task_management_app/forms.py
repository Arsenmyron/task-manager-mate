from django import forms
from django.contrib.auth.forms import UserCreationForm

from task_management_app.models import (
    Task,
    Worker,
    Tag,
    TaskType,
    Position
)


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = (
            "name",
            "description",
            "deadline",
            "priority",
            "task_type",
            "assignees",
            "tags"
        )

        widgets = {
            "deadline": forms.DateInput(attrs={"type": "date"}),
            "task_type": forms.RadioSelect,
            "assignees": forms.CheckboxSelectMultiple,
            "tags": forms.CheckboxSelectMultiple,
        }


class WorkerForm(UserCreationForm):
    class Meta:
        model = Worker
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "position",
        )
        widgets = {
            "email": forms.EmailInput(),
            "position": forms.Select(),
        }


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ("name",)


class TaskTypeForm(forms.ModelForm):
    class Meta:
        model = TaskType
        fields = ("name",)


class PositionForm(forms.ModelForm):
    class Meta:
        model = Position
        fields = ("name",)