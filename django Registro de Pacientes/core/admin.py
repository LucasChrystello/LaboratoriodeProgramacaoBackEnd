from django.contrib import admin
from .models import Paciente, Atendimento, Matricula

@admin.register(Matricula)
class MatriculaAdmin(admin.ModelAdmin):
    list_display = ['numero', 'disponivel', 'usuario', 'data_criacao', 'data_utilizacao']
    list_filter = ['disponivel', 'data_criacao']
    search_fields = ['numero', 'usuario__username']
    readonly_fields = ['data_criacao', 'data_utilizacao']
    
    fieldsets = (
        ('Informações da Matrícula', {
            'fields': ('numero', 'disponivel', 'usuario')
        }),
        ('Datas', {
            'fields': ('data_criacao', 'data_utilizacao'),
            'classes': ('collapse',)
        }),
    )

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'telefone', 'data_nascimento']

@admin.register(Atendimento)
class AtendimentoAdmin(admin.ModelAdmin):
    list_display = ['paciente', 'data_consulta']