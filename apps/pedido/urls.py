from django.urls import path

from apps.pedido import views


app_name = 'pedido'


urlpatterns = [
    path('pedidos/', views.PedidoListView.as_view(), name='pedido_list'),
    path('pedidos/<int:pk>/', views.PedidoDetailView.as_view(), name='pedido_detail'),
]
