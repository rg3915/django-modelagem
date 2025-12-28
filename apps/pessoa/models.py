from django.db import models
from django.urls import reverse

from apps.core.models import BaseModel


class Cliente(BaseModel):
    nome = models.CharField('nome', max_length=100)
    email = models.EmailField('e-mail')
    telefone = models.CharField('telefone', max_length=20, blank=True, null=True)

    class Meta:
        ordering = ('nome',)
        verbose_name = 'cliente'
        verbose_name_plural = 'clientes'

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('pessoa:cliente_detail', kwargs={'pk': self.pk})
