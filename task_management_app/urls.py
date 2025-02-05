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
    PositionListView,
    PositionDeleteView,
    TaskTypeListView,
    TaskTypeDeleteView,
    TagListView,
    TagDeleteView,
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
        "tags/", TagListView.as_view(), name="tag-list"
    ),
    path(
        "tag/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"
    ),
    path(
        "task_type/create/", TaskTypeCreateView.as_view(), name="task-type-create"
    ),
    path(
        "task_types/", TaskTypeListView.as_view(), name="task-type-list"
    ),
    path(
        "task_type/<int:pk>/delete/", TaskTypeDeleteView.as_view(), name="task-type-delete"
    ),
    path(
        "position/create/", PositionCreateView.as_view(), name="position-create"
    ),
    path(
        "positions/", PositionListView.as_view(), name="position-list"
    ),
    path(
        "position/<int:pk>/delete/", PositionDeleteView.as_view(), name="position-delete"
    ),
    path(
        "workers/", WorkerListView.as_view(), name="worker-list"
    ),
    path(
        "tasks/completed/", CompletedTaskListView.as_view(), name="completed-task-list"
    ),

]

app_name = "task_management_app"
