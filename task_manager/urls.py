from django.urls import path, include
from django.contrib import admin

from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("task_management_app.urls", namespace="task-management-app")),
    path("accounts/", include("django.contrib.auth.urls")),
] + debug_toolbar_urls()
