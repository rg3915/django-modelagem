from django.views.generic import DetailView, ListView

from apps.pedido.models import Pedido


class PedidoListView(ListView):
    model = Pedido
    paginate_by = 20


class PedidoDetailView(DetailView):
    model = Pedido
