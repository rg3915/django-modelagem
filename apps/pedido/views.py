from django.views.generic import ListView

from apps.pedido.models import Pedido


class PedidoListView(ListView):
    model = Pedido
    paginate_by = 20
