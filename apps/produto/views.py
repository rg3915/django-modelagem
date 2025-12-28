from django.views.generic import CreateView, DetailView, ListView, UpdateView

from apps.produto.forms import ProdutoForm
from apps.produto.models import Produto


class ProdutoListView(ListView):
    model = Produto
    paginate_by = 20


class ProdutoDetailView(DetailView):
    model = Produto
    context_object_name = 'produto'
    slug_field = 'uuid'
    slug_url_kwarg = 'uuid'


class ProdutoCreateView(CreateView):
    model = Produto
    form_class = ProdutoForm


class ProdutoUpdateView(UpdateView):
    model = Produto
    form_class = ProdutoForm
    slug_field = 'uuid'
    slug_url_kwarg = 'uuid'
