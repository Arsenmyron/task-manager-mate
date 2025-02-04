from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from task_management_app.forms import TaskForm
from task_management_app.models import Task


class TaskListView(generic.ListView):
    model = Task
    context_object_name = "task_list"
    template_name = "task_management_app/task_list.html"


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


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("task_management_app:task-list")

