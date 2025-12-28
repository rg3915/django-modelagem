from django.contrib import admin

from apps.pedido.models import Pedido, PedidoItem


class PedidoItemInline(admin.TabularInline):
    model = PedidoItem
    extra = 0
    fields = ('produto', 'quantidade', 'preco')


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'id', 'cliente', 'status', 'data', 'ativo')
    search_fields = ('cliente__nome',)
    list_filter = ('status', 'ativo', 'data')
    readonly_fields = ('uuid', 'criado_em', 'modificado_em')
    inlines = [PedidoItemInline]
    autocomplete_fields = ('cliente',)
