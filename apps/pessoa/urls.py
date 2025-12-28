from django.urls import path

from apps.pessoa import views


app_name = 'pessoa'


urlpatterns = [
    path('clientes/', views.ClienteListView.as_view(), name='cliente_list'),
]
