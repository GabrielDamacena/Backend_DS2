from django.urls import path
from .views import UsuarioListCreateView, UsuarioDetailView, PontoRegistroView, PontoDetailView

urlpatterns = [
    # URLs para Usuario
    path('api/usuarios/', UsuarioListCreateView.as_view(), name='usuario-list-create'),
    path('api/usuarios/<int:pk>/', UsuarioDetailView.as_view(), name='usuario-detail'),

    # URLs para Ponto
    path('api/pontos/', PontoRegistroView.as_view(), name='ponto-list-create'),
    path('api/pontos/<int:pk>/', PontoDetailView.as_view(), name='ponto-detail'),

    
]
