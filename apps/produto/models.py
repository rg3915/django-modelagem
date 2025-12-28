from django.db import models
from django.urls import reverse

from apps.core.models import BaseModel


class Categoria(BaseModel):
    titulo = models.CharField('título', max_length=100)

    class Meta:
        ordering = ('titulo',)
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__(self):
        return self.titulo


class Produto(BaseModel):
    sku = models.CharField('SKU', max_length=50, unique=True)
    titulo = models.CharField('título', max_length=200)
    preco = models.DecimalField('preço', max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT,
        verbose_name='categoria',
        related_name='produtos'
    )

    class Meta:
        ordering = ('titulo',)
        verbose_name = 'produto'
        verbose_name_plural = 'produtos'

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('produto:produto_detail', kwargs={'uuid': self.uuid})
