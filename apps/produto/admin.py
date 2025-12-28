from django.contrib import admin

from apps.produto.models import Categoria, Produto


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'ativo')
    search_fields = ('titulo',)
    list_filter = ('ativo',)
    readonly_fields = ('uuid', 'criado_em', 'modificado_em')


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('sku', 'titulo', 'preco', 'categoria', 'ativo')
    search_fields = ('sku', 'titulo')
    list_filter = ('categoria', 'ativo')
    readonly_fields = ('uuid', 'criado_em', 'modificado_em')
    autocomplete_fields = ('categoria',)
