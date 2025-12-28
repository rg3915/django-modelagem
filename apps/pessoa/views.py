from django.views.generic import DetailView, ListView

from apps.pessoa.models import Cliente


class ClienteListView(ListView):
    model = Cliente
    paginate_by = 20

    # def get_queryset(self):
    #     return Cliente.objects.filter(ativo=True)


class ClienteDetailView(DetailView):
    model = Cliente
    context_object_name = 'cliente'
