from django.urls import path

from apps.pedido import views


app_name = 'pedido'


urlpatterns = [
    path('pedidos/', views.PedidoListView.as_view(), name='pedido_list'),
    path('pedidos/criar/', views.PedidoCreateView.as_view(), name='pedido_create'),
    path('pedidos/<int:pk>/', views.PedidoDetailView.as_view(), name='pedido_detail'),
    path('pedidos/<int:pk>/editar/', views.PedidoUpdateView.as_view(), name='pedido_update'),
]
