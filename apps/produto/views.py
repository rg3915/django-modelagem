from django.views.generic import ListView

from apps.produto.models import Produto


class ProdutoListView(ListView):
    model = Produto
    paginate_by = 20
