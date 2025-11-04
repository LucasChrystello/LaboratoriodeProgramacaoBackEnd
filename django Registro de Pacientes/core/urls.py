from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pacientes/', views.lista_pacientes, name='lista_pacientes'),
    path('pacientes/novo/', views.novo_paciente, name='novo_paciente'),
    path('pacientes/editar/<int:paciente_id>/', views.editar_paciente, name='editar_paciente'),
    path('pacientes/excluir/<int:paciente_id>/', views.excluir_paciente, name='excluir_paciente'),
    
    # URLs para atendimentos
    path('atendimentos/', views.lista_atendimentos, name='lista_atendimentos'),
    path('atendimentos/novo/', views.novo_atendimento, name='novo_atendimento'),
    path('atendimentos/editar/<int:atendimento_id>/', views.editar_atendimento, name='editar_atendimento'),
    path('atendimentos/excluir/<int:atendimento_id>/', views.excluir_atendimento, name='excluir_atendimento'),
    
    # URLs para relatórios
    path('relatorios/', views.relatorios, name='relatorios'),
    path('relatorios/pdf/', views.relatorio_pdf, name='relatorio_pdf'),
]