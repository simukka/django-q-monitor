from django.views.generic.list import ListView
from django_q.models import OrmQ

class OrmQListView(ListView):
    model = OrmQ
    paginate_by = 100
    ordering = '-pk'

