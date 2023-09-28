from django.urls import path
from . import views


urlpatterns = [

    path('', views.index, name='index'),
    path('saida/', views.saida, name='saida'),
    path('senha/', views.senha, name='senha'),
    path('entrega/', views.entrega, name='entrega'),
    path('empresa/', views.empresa, name='empresa'),
    path('relatorio/', views.relatorio, name='relatorio'),
    path('tecnico/', views.tecnico, name='tecnico'),
    path('equipamento/', views.equipamento, name='equipamento'),
    path('autorizacao/', views.autorizacao, name='autorizacao'),
    path('relatorio_saida/', views.relatorio_saida, name='relatorio_saida'),
    path('relatorio_entrega/', views.relatorio_entrega, name='relatorio_entrega'),
    path('relatorio_saida_total/', views.rel_saida_total, name='rel_saida_total'),
    path('relatorio_entrega_total/', views.rel_entrega_total, name='rel_entrega_total'),
    #path('gerar-numero-cupom/', views.gerar_numero_cupom, name='gerar_numero_cupom'),
    path('verificar_cupom_saida/', views.verificar_cupom_saida, name='verificar_cupom_saida'),
    path('verificar_cupom_entrega/', views.verificar_cupom_entrega, name='verificar_cupom_entrega'),
]