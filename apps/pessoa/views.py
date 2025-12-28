from django.views.generic import CreateView, DetailView, ListView, UpdateView

from apps.pessoa.forms import ClienteForm
from apps.pessoa.models import Cliente


class ClienteListView(ListView):
    model = Cliente
    paginate_by = 20

    # def get_queryset(self):
    #     return Cliente.objects.filter(ativo=True)


class ClienteDetailView(DetailView):
    model = Cliente
    context_object_name = 'cliente'


class ClienteCreateView(CreateView):
    model = Cliente
    form_class = ClienteForm


class ClienteUpdateView(UpdateView):
    model = Cliente
    form_class = ClienteForm
