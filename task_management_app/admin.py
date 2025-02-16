from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from task_management_app.models import TaskType, Task, Position, Tag, Worker


class WorkerAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("position", )

    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("position", )}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("position", )}),
    )


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("name", "deadline", "priority", "is_completed")


admin.site.register(TaskType)
admin.site.register(Position)
admin.site.register(Tag)
admin.site.register(Worker, WorkerAdmin)
