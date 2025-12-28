from django import forms

from apps.produto.models import Produto


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ('sku', 'titulo', 'preco', 'categoria')
