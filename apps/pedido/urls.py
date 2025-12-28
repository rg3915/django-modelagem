from django.urls import path

from apps.pedido import views


app_name = 'pedido'


urlpatterns = [
    path('pedidos/', views.PedidoListView.as_view(), name='pedido_list'),
]
