from django.urls import path

from task_management_app.views import (
    TaskListView,
    TaskCreateView,
    TaskDetailView,
    TaskUpdateView,
    TaskDeleteView,
    TagCreateView,
    TaskTypeCreateView,
    PositionCreateView,
)

urlpatterns = [
    path(
        "", TaskListView.as_view(), name="task-list"
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
        "tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"
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

]

app_name = "task_management_app"