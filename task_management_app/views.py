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
    Tag, Worker
)


class TaskListView(generic.ListView):
    model = Task
    context_object_name = "task_list"
    ordering = ["is_completed", "priority"]
    template_name = "task_management_app/home.html"

    def get_queryset(self):
        return Task.objects.filter(is_completed=False)


class CompletedTaskListView(generic.ListView):
    model = Task
    context_object_name = "completed_task_list"
    template_name = "task_management_app/completed_task_list.html"

    def get_queryset(self):
        return Task.objects.filter(is_completed=True)


class TaskDetailView(generic.DetailView):
    model = Task
    context_object_name = "task"
    template_name = "task_management_app/task_detail.html"


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("task_management_app:home")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("task_management_app:home")


class TaskToggleStatusView(View):
    def post(self, request, *args, **kwargs):
        task = Task.objects.get(pk=kwargs["pk"])
        task.is_completed = not task.is_completed
        task.save()
        return redirect("task-management:home")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("task_management_app:completed-task-list")


class WorkerSignUpView(generic.CreateView):
    form_class = WorkerForm
    success_url = reverse_lazy("task_management_app:home")
    template_name = "registration/signup.html"


class WorkerListView(generic.ListView):
    model = Worker
    context_object_name = "worker_list"
    template_name = "task_management_app/worker_list.html"

class TagCreateView(generic.CreateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("task_management_app:home")
    template_name = "task_management_app/tag_form.html"


class TagListView(generic.ListView):
    model = Tag
    context_object_name = "tag_list"
    template_name = "task_management_app/tag_list.html"


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("task_management_app:tag-list")


class TaskTypeCreateView(generic.CreateView):
    model = TaskType
    form_class = TaskTypeForm
    success_url = reverse_lazy("task_management_app:home")
    template_name = "task_management_app/task_type_form.html"


class TaskTypeListView(generic.ListView):
    model = TaskType
    context_object_name = "task_type_list"
    template_name = "task_management_app/task_type_list.html"

class TaskTypeDeleteView(generic.DeleteView):
    model = TaskType
    success_url = reverse_lazy("task_management_app:task-type-list")

class PositionCreateView(generic.CreateView):
    model = Position
    form_class = PositionForm
    success_url = reverse_lazy("task_management_app:home")
    template_name = "task_management_app/position_form.html"


class PositionListView(generic.ListView):
    model = Position
    context_object_name = "position_list"
    template_name = "task_management_app/position_list.html"


class PositionDeleteView(generic.DeleteView):
    model = Position
    success_url = reverse_lazy("task_management_app:position-list")