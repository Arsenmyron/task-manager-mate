from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from task_management_app.models import Task, Worker


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


class WorkerCreationForm(UserCreationForm):
    class Meta:
        model = Worker
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "position",
            "password",
        )
        widgets = {
            "email": forms.EmailInput(),
            "position": forms.Select(),
            "password": forms.PasswordInput(),
        }


class WorkerChangeForm(UserChangeForm):
    class Meta:
        model = Worker
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password",
        )

        widgets = {
            "email": forms.EmailInput(),
            "position": forms.Select(),
            "password": forms.PasswordInput(),
        }