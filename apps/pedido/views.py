from django.db import transaction
from django.views.generic import CreateView, DetailView, ListView

from apps.pedido.forms import PedidoForm
from apps.pedido.models import Pedido, PedidoItem
from apps.produto.models import Produto


class PedidoListView(ListView):
    model = Pedido
    paginate_by = 20


class PedidoDetailView(DetailView):
    model = Pedido


class PedidoCreateView(CreateView):
    model = Pedido
    form_class = PedidoForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['produtos'] = Produto.objects.filter(ativo=True).order_by('titulo')
        return context

    @transaction.atomic
    def form_valid(self, form):
        # Salva o pedido
        self.object = form.save()

        # Processa os itens do pedido
        post_data = self.request.POST
        item_count = 0

        # Identifica quantos itens foram enviados
        while f'itens-{item_count}-produto' in post_data:
            produto_id = post_data.get(f'itens-{item_count}-produto')
            quantidade = post_data.get(f'itens-{item_count}-quantidade')
            preco = post_data.get(f'itens-{item_count}-preco')

            if produto_id and quantidade and preco:
                PedidoItem.objects.create(
                    pedido=self.object,
                    produto_id=produto_id,
                    quantidade=quantidade,
                    preco=preco
                )

            item_count += 1

        return super().form_valid(form)
