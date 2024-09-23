from django.urls import path
from .views.tasks import TaskListView, TaskFailureListView, TaskSuccessListView
from .views.ormq import OrmQListView

urlpatterns = [
    path('tasks', TaskListView.as_view(), name='tasks_list'),
    path('tasks/success', TaskSuccessListView.as_view(), name='tasks_success_list'),
    path('tasks/failure', TaskFailureListView.as_view(), name='tasks_failure_list'),
    path('orm', OrmQListView.as_view(), name='ormq_list')
]