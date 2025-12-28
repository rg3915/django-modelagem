from django.contrib import admin

from apps.pessoa.models import Cliente


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone', 'ativo')
    search_fields = ('nome', 'email')
    list_filter = ('ativo',)
    readonly_fields = ('uuid', 'criado_em', 'modificado_em')
