from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
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


def index(request):
    return render(request, "task_management_app/index.html")


class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    context_object_name = "task_list"
    ordering = ["is_completed", "priority"]
    template_name = "task_management_app/home.html"

    def get_queryset(self):
        return (Task.objects.select_related(
            "task_type"
        ).filter(
            is_completed=False
        ))


class TaskCompletedListView(LoginRequiredMixin, generic.ListView):
    model = Task
    context_object_name = "completed_task_list"
    template_name = "task_management_app/completed_task_list.html"

    def get_queryset(self):
        return Task.objects.filter(is_completed=True)


class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    model = Task
    context_object_name = "task"
    template_name = "task_management_app/task_detail.html"

    def get_queryset(self):
        return Task.objects.select_related(
            "task_type"
        ).prefetch_related(
            "assignees",
            "tags"
        )


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("task_management_app:home")


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("task_management_app:home")


class TaskToggleStatusView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        task = Task.objects.get(pk=kwargs["pk"])
        if task.is_completed:
            task.is_completed = False
            task.save()
            return redirect("task_management_app:completed-task-list")
        else:
            task.is_completed = True
            task.save()
            return redirect("task-management-app:home")


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    success_url = reverse_lazy("task_management_app:completed-task-list")


class WorkerSignUpView(generic.CreateView):
    form_class = WorkerForm
    success_url = reverse_lazy("task_management_app:home")
    template_name = "registration/signup.html"


class WorkerListView(LoginRequiredMixin, generic.ListView):
    model = Worker
    context_object_name = "worker_list"
    template_name = "task_management_app/worker_list.html"

    def get_queryset(self):
        return Worker.objects.prefetch_related("tasks")


class WorkerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Worker
    template_name = "task_management_app/worker_detail.html"

    def get_queryset(self):
        return Worker.objects.select_related(
            "position"
        ).prefetch_related(
            "tasks"
        )


class TagCreateView(LoginRequiredMixin, generic.CreateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("task_management_app:home")
    template_name = "task_management_app/tag_form.html"


class TagListView(LoginRequiredMixin, generic.ListView):
    model = Tag
    context_object_name = "tag_list"
    template_name = "task_management_app/tag_list.html"


class TagDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("task_management_app:tag-list")


class TaskTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = TaskType
    form_class = TaskTypeForm
    success_url = reverse_lazy("task_management_app:home")
    template_name = "task_management_app/task_type_form.html"


class TaskTypeListView(LoginRequiredMixin, generic.ListView):
    model = TaskType
    context_object_name = "task_type_list"
    template_name = "task_management_app/task_type_list.html"


class TaskTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = TaskType
    success_url = reverse_lazy("task_management_app:task-type-list")


class PositionCreateView(LoginRequiredMixin, generic.CreateView):
    model = Position
    form_class = PositionForm
    success_url = reverse_lazy("task_management_app:home")
    template_name = "task_management_app/position_form.html"


class PositionListView(LoginRequiredMixin, generic.ListView):
    model = Position
    context_object_name = "position_list"
    template_name = "task_management_app/position_list.html"


class PositionDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Position
    success_url = reverse_lazy("task_management_app:position-list")
