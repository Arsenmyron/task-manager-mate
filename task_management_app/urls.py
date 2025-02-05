from django.urls import path

from task_management_app.views import (
    TaskListView,
    TaskCreateView,
    TaskDetailView,
    TaskUpdateView,
    TaskDeleteView,
    WorkerSignUpView,
    TagCreateView,
    TaskTypeCreateView,
    PositionCreateView,
    TaskToggleStatusView,
    WorkerListView,
    CompletedTaskListView,
)

urlpatterns = [
    path(
        "", TaskListView.as_view(), name="home"
    ),
    path(
        "tasks/create/", TaskCreateView.as_view(), name="task-create"
    ),
    path(
        "tasks/<int:pk>/", TaskDetailView.as_view(), name="task-detail"
    ),
    path(
        "tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"
    ),
    path(
        "task_toggle_status/<int:pk>/", TaskToggleStatusView.as_view(), name="task-toggle-status"
    ),
    path(
        "tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"
    ),
    path(
        "signup/", WorkerSignUpView.as_view(), name="signup"
    ),
    path(
        "tag/create/", TagCreateView.as_view(), name="tag-create"
    ),
    path(
        "task_type/create/", TaskTypeCreateView.as_view(), name="task-type-create"
    ),
    path(
        "position/create/", PositionCreateView.as_view(), name="position-create"
    ),
    path(
        "workers/", WorkerListView.as_view(), name="worker-list"
    ),
    path(
        "tasks/completed/", CompletedTaskListView.as_view(), name="completed-task-list"
    ),

]

app_name = "task_management_app"