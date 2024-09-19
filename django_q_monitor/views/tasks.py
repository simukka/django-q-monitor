from django.views.generic.detail import SingleObjectMixin, DetailView
from django.views.generic.base import TemplateView, ContextMixin, View
from django.views.generic.list import MultipleObjectMixin, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils.decorators import classonlymethod
from django.http import HttpResponse
from django.urls import reverse_lazy
from django_q.models import Task, Schedule, OrmQ, Failure, Success

class TaskListView(ListView):
    model = Task
    paginate_by = 100
    ordering = '-pk'

class TaskFailureListView(ListView):
    model = Failure
    paginate_by = 100

class TaskSuccessListView(ListView):
    model = Success
    paginate_by = 100

class TaskDetailView(DetailView):
    model = Task