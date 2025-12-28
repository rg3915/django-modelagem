from django.urls import path

from apps.produto import views


app_name = 'produto'


urlpatterns = [
    path('produtos/', views.ProdutoListView.as_view(), name='produto_list'),
    path('produtos/criar/', views.ProdutoCreateView.as_view(), name='produto_create'),
    path('produtos/<str:uuid>/', views.ProdutoDetailView.as_view(), name='produto_detail'),
    path('produtos/<str:uuid>/editar/', views.ProdutoUpdateView.as_view(), name='produto_update'),
]
