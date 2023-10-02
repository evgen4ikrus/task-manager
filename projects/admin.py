from django.contrib import admin
from django.db.models import Prefetch

from .models import Comment, Employee, Position, Project, Task


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('title', )


class CommentInline(admin.TabularInline):
    model = Comment


class TaskInline(admin.TabularInline):
    model = Task


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'position')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'manager', 'status')
    list_filter = ('status', )
    search_fields = ('title', )
    inlines = [TaskInline]


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'deadline', 'status')
    list_filter = ('status', )
    search_fields = ('title', )
    inlines = [CommentInline]
