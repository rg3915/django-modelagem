from django import forms

from apps.pedido.models import Pedido


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ('cliente', 'status', 'data')
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
        }
