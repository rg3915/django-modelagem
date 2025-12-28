from django import forms

from apps.pessoa.models import Cliente


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('nome', 'email', 'telefone')
