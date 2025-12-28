from django.views.generic import DetailView, ListView

from apps.produto.models import Produto


class ProdutoListView(ListView):
    model = Produto
    paginate_by = 20


class ProdutoDetailView(DetailView):
    model = Produto
    template_name = 'produto/produto_detail.html'
    context_object_name = 'produto'
    slug_field = 'uuid'
    slug_url_kwarg = 'uuid'
