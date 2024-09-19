from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django_q.models import Task, Failure, Success

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