from django.core.validators import MinValueValidator
from django.db import models
from django.urls import reverse

from apps.core.models import BaseModel
from apps.pessoa.models import Cliente
from apps.produto.models import Produto


class Pedido(BaseModel):
    class StatusChoices(models.TextChoices):
        PENDENTE = 'PE', 'Pendente'
        EM_ANDAMENTO = 'AN', 'Em Andamento'
        APROVADO = 'AP', 'Aprovado'
        CANCELADO = 'CA', 'Cancelado'

    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.PROTECT,
        verbose_name='cliente',
        related_name='pedidos'
    )
    status = models.CharField(
        'status',
        max_length=2,
        choices=StatusChoices.choices,
        default=StatusChoices.PENDENTE
    )
    data = models.DateField('data', null=True, blank=True)

    class Meta:
        ordering = ('-data',)
        verbose_name = 'pedido'
        verbose_name_plural = 'pedidos'

    def __str__(self):
        return f'Pedido {self.pk} - {self.cliente.nome}'

    def get_absolute_url(self):
        return reverse('pedido:pedido_detail', kwargs={'pk': self.pk})


class PedidoItem(models.Model):
    pedido = models.ForeignKey(
        Pedido,
        on_delete=models.CASCADE,
        verbose_name='pedido',
        related_name='itens'
    )
    produto = models.ForeignKey(
        Produto,
        on_delete=models.PROTECT,
        verbose_name='produto',
        related_name='pedido_itens'
    )
    quantidade = models.PositiveIntegerField(
        'quantidade',
        validators=[MinValueValidator(1)]
    )
    preco = models.DecimalField('preço', max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'item do pedido'
        verbose_name_plural = 'itens do pedido'

    def __str__(self):
        return f'{self.produto.titulo} - {self.quantidade}x'
