from django.views.generic import ListView

from apps.pessoa.models import Cliente


class ClienteListView(ListView):
    model = Cliente
    context_object_name = 'clientes'
    paginate_by = 20

    # def get_queryset(self):
    #     return Cliente.objects.filter(ativo=True)
