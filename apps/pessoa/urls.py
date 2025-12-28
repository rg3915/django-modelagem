from django.urls import path

from apps.pessoa import views


app_name = 'pessoa'


urlpatterns = [
    path('clientes/', views.ClienteListView.as_view(), name='cliente_list'),
    path('clientes/criar/', views.ClienteCreateView.as_view(), name='cliente_create'),
    path('clientes/<int:pk>/', views.ClienteDetailView.as_view(), name='cliente_detail'),
    path('clientes/<int:pk>/editar/', views.ClienteUpdateView.as_view(), name='cliente_update'),
]
