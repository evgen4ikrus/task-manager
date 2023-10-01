from django.views.generic import DetailView, ListView

from projects.models import Project, Task


class ProjectListView(ListView):
    model = Project
    paginate_by = 50
    template_name = 'project_list.html'
    context_object_name = 'projects'

    def get_context_data(self, **kwargs):
        context = super(ProjectListView, self).get_context_data(**kwargs)
        context['projects'] = context['projects'].select_related('manager')
        return context


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'project_detail.html'
    context_object_name = 'project'

    def get_context_data(self, **kwargs):
        context = super(ProjectDetailView, self).get_context_data(**kwargs)
        context['tasks'] = context['object'].tasks.all()
        return context


class TaskDetailView(DetailView):
    model = Task
    template_name = 'task_detail.html'
    context_object_name = 'task'

    def get_context_data(self, **kwargs):
        context = super(TaskDetailView, self).get_context_data(**kwargs)
        context['employees'] = context['object'].performers.all().select_related('position')
        return context
