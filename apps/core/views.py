from django.shortcuts import render


def index(request):
    template_name = 'index.html'
    # Importa os modelos quando estiverem criados
    try:
        from apps.pessoa.models import Cliente
        total_clientes = Cliente.objects.count()
    except:
        total_clientes = 0

    try:
        from apps.produto.models import Produto
        total_produtos = Produto.objects.count()
    except:
        total_produtos = 0

    try:
        from apps.pedido.models import Pedido
        total_pedidos = Pedido.objects.count()
    except:
        total_pedidos = 0

    context = {
        'total_clientes': total_clientes,
        'total_produtos': total_produtos,
        'total_pedidos': total_pedidos,
    }
    return render(request, template_name, context)
