from django.urls import path
from .views import UsuarioListCreateView, UsuarioDetailView, PontoRegistroView, PontoDetailView,ComparePhotoView,RelatorioPontoPDFView,RelatorioPontoExcelView

urlpatterns = [
    # URLs para Usuario
    path('api/usuarios/', UsuarioListCreateView.as_view(), name='usuario-list-create'),
    path('api/usuarios/<int:pk>/', UsuarioDetailView.as_view(), name='usuario-detail'),

    # URLs para Ponto
    path('api/pontos/', PontoRegistroView.as_view(), name='ponto-list-create'),
    path('api/pontos/<int:pk>/', PontoDetailView.as_view(), name='ponto-detail'),

    #URL para comparar foto
    path('compare-photo/', ComparePhotoView.as_view(), name='compare-photo'),

    #URLS para criar relatorios
    path('relatorio-pontos-pdf/', RelatorioPontoPDFView.as_view(), name='relatorio_pontos'),
    path('relatorio-pontos-excel/', RelatorioPontoExcelView.as_view(), name='relatorio_pontos_excel'),
]

    
