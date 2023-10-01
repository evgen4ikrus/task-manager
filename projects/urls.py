from django.urls import path

from projects.views import ProjectDetailView, ProjectListView, TaskDetailView

urlpatterns = [
    path('', ProjectListView.as_view(), name="project-list"),
    path('<int:pk>/', ProjectDetailView.as_view(), name="project-detail"),
    path('task/<int:pk>/', TaskDetailView.as_view(), name="task-detail"),
]
