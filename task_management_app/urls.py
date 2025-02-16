from django.urls import path

from task_management_app.views import (
    index,
    WorkerSignUpView,
    WorkerListView,
    WorkerDetailView,
    TaskListView,
    TaskCreateView,
    TaskDetailView,
    TaskUpdateView,
    TaskDeleteView,
    TaskCompletedListView,
    TaskTypeCreateView,
    TaskTypeListView,
    TaskTypeDeleteView,
    TaskToggleStatusView,
    PositionCreateView,
    PositionListView,
    PositionDeleteView,
    TagCreateView,
    TagListView,
    TagDeleteView
)

urlpatterns = [
    path(
        "", index, name="index"
    ),
    path(
        "tasks/", TaskListView.as_view(), name="home"
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
        "tasks/<int:pk>/toggle-status/",
        TaskToggleStatusView.as_view(),
        name="task-toggle-status"
    ),
    path(
        "tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"
    ),
    path(
        "signup/", WorkerSignUpView.as_view(), name="signup"
    ),
    path(
        "tags/create/", TagCreateView.as_view(), name="tag-create"
    ),
    path(
        "tags/", TagListView.as_view(), name="tag-list"
    ),
    path(
        "tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"
    ),
    path(
        "task-types/create/",
        TaskTypeCreateView.as_view(),
        name="task-type-create"
    ),
    path(
        "task-types/", TaskTypeListView.as_view(), name="task-type-list"
    ),
    path(
        "task-types/<int:pk>/delete/",
        TaskTypeDeleteView.as_view(),
        name="task-type-delete"
    ),
    path(
        "positions/create/",
        PositionCreateView.as_view(),
        name="position-create"
    ),
    path(
        "positions/",
        PositionListView.as_view(),
        name="position-list"
    ),
    path(
        "positions/<int:pk>/delete/",
        PositionDeleteView.as_view(),
        name="position-delete"
    ),
    path(
        "workers/", WorkerListView.as_view(), name="worker-list"
    ),
    path(
        "workers/<int:pk>/",
        WorkerDetailView.as_view(),
        name="worker-detail"
    ),
    path(
        "tasks/completed/",
        TaskCompletedListView.as_view(),
        name="completed-task-list"
    ),

]

app_name = "task_management_app"
