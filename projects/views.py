from django.views.generic import DetailView, ListView
from django.views.generic.edit import ModelFormMixin

from projects.forms import CommentForm
from projects.models import Comment, Project, Task


class ProjectListView(ListView):
    model = Project
    paginate_by = 50
    template_name = 'project_list.html'
    context_object_name = 'projects'
    requested_project_status = 'all'

    def get_context_data(self, **kwargs):
        context = super(ProjectListView, self).get_context_data(**kwargs)
        context['statuses'] = dict(Project.STATUSES)
        context['requested_project_status'] = self.requested_project_status
        return context

    def get_queryset(self, **kwargs):
        project_status = self.request.GET.get("project_status")
        if project_status:
            ProjectListView.requested_project_status = project_status
        if ProjectListView.requested_project_status == 'all':
            return super(ProjectListView, self).get_queryset().all().select_related('manager')
        return super(ProjectListView, self).get_queryset().filter(
            status=ProjectListView.requested_project_status).select_related('manager')



class ProjectDetailView(DetailView):
    model = Project
    template_name = 'project_detail.html'
    context_object_name = 'project'

    def get_context_data(self, **kwargs):
        context = super(ProjectDetailView, self).get_context_data(**kwargs)
        context['tasks'] = context['object'].tasks.all()
        return context

    def get_queryset(self):
        queryset = super(ProjectDetailView, self).get_queryset().select_related('manager')
        return queryset


class TaskDetailView(ModelFormMixin, DetailView):
    model = Task
    template_name = 'task_detail.html'
    context_object_name = 'task'
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super(TaskDetailView, self).get_context_data(**kwargs)
        context['employees'] = context['object'].performers.all().select_related('position')
        context['comments'] = context['object'].comments.all()
        return context

    def get_queryset(self):
        queryset = super(TaskDetailView, self).get_queryset().select_related('project').prefetch_related('comments')
        return queryset

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            comment = form.cleaned_data
            Comment.objects.create(
                text=comment['text'],
                author=comment['author'],
                task=self.object
            )
            return super(TaskDetailView, self).form_valid(form)
        else:
            return self.form_invalid(form)
