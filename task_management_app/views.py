from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic, View
from task_management_app.forms import (
    TaskForm,
    WorkerForm,
    TagForm,
    TaskTypeForm,
    PositionForm
)

from task_management_app.models import (
    Task,
    Position,
    TaskType,
    Tag
)


class TaskListView(generic.ListView):
    model = Task
    context_object_name = "task_list"
    ordering = ["is_completed"]
    template_name = "task_management_app/home.html"


class TaskDetailView(generic.DetailView):
    model = Task
    context_object_name = "task"
    template_name = "task_management_app/task_detail.html"


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("task_management_app:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("task_management_app:task-list")


class TaskToggleStatusView(View):
    def post(self, request, *args, **kwargs):
        task = Task.objects.get(pk=kwargs["pk"])
        task.is_completed = not task.is_completed
        task.save()
        return redirect("task-management:home")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("task_management_app:task-list")


class WorkerSignUpView(generic.CreateView):
    form_class = WorkerForm
    success_url = reverse_lazy("task_management_app:task-list")
    template_name = "registration/signup.html"


class TagCreateView(generic.CreateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("task_management_app:task-list")
    template_name = "task_management_app/tag_form.html"


class TaskTypeCreateView(generic.CreateView):
    model = TaskType
    form_class = TaskTypeForm
    success_url = reverse_lazy("task_management_app:task-list")
    template_name = "task_management_app/task_type_form.html"


class PositionCreateView(generic.CreateView):
    model = Position
    form_class = PositionForm
    success_url = reverse_lazy("task_management_app:task-list")
    template_name = "task_management_app/position_form.html"