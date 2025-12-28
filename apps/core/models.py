import uuid

from django.conf import settings
from django.db import models


class UuidModel(models.Model):
    uuid = models.UUIDField(unique=True, editable=False, default=uuid.uuid4)

    class Meta:
        abstract = True


class TimeStampedModel(models.Model):
    criado_em = models.DateTimeField('criado em', auto_now_add=True, auto_now=False)
    modificado_em = models.DateTimeField('modificado em', auto_now_add=False, auto_now=True)

    class Meta:
        abstract = True


class CriadoPor(models.Model):
    criado_por = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='criado por', null=True, blank=True
    )

    class Meta:
        abstract = True


class Ativo(models.Model):
    ativo = models.BooleanField('ativo', default=True)

    class Meta:
        abstract = True


class BaseModel(UuidModel, TimeStampedModel, Ativo):
    class Meta:
        abstract = True
