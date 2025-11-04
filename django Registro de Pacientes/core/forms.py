from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Paciente, Atendimento, Matricula
from django.utils import timezone

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True, label='Nome')
    last_name = forms.CharField(max_length=30, required=True, label='Sobrenome')
    matricula = forms.CharField(
        max_length=20, 
        required=True, 
        label='Número da Matrícula',
        help_text='Digite a matrícula fornecida pela administração do sistema.'
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'matricula']

    def clean_matricula(self):
        matricula_numero = self.cleaned_data.get('matricula')
        
        # Verificar se a matrícula existe
        try:
            matricula_obj = Matricula.objects.get(numero=matricula_numero)
        except Matricula.DoesNotExist:
            raise forms.ValidationError("Matrícula não encontrada no sistema. Verifique o número e tente novamente.")
        
        # Verificar se a matrícula está disponível
        if not matricula_obj.disponivel:
            raise forms.ValidationError("Esta matrícula já está em uso. Contacte a administração.")
        
        return matricula_numero

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        
        if commit:
            user.save()
            # Atualizar a matrícula para marcar como utilizada
            matricula_numero = self.cleaned_data['matricula']
            matricula_obj = Matricula.objects.get(numero=matricula_numero)
            matricula_obj.disponivel = False
            matricula_obj.usuario = user
            matricula_obj.data_utilizacao = timezone.now()
            matricula_obj.save()
        
        return user

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nome', 'email', 'telefone', 'data_nascimento', 'endereco']
        widgets = {
            'data_nascimento': forms.DateInput(attrs={'type': 'date'}),
            'endereco': forms.Textarea(attrs={'rows': 3}),
        }
        labels = {
            'nome': 'Nome Completo',
            'email': 'E-mail',
            'telefone': 'Telefone',
            'data_nascimento': 'Data de Nascimento',
            'endereco': 'Endereço',
        }

class AtendimentoForm(forms.ModelForm):
    class Meta:
        model = Atendimento
        fields = ['paciente', 'data_consulta', 'diagnostico', 'prescricao']
        widgets = {
            'data_consulta': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'diagnostico': forms.Textarea(attrs={
                'rows': 4, 
                'placeholder': 'Descreva o diagnóstico do paciente...'
            }),
            'prescricao': forms.Textarea(attrs={
                'rows': 4, 
                'placeholder': 'Descreva a prescrição médica, medicamentos, tratamentos...'
            }),
        }
        labels = {
            'paciente': 'Paciente',
            'data_consulta': 'Data e Hora da Consulta',
            'diagnostico': 'Diagnóstico',
            'prescricao': 'Prescrição Médica',
        }
        help_texts = {
            'data_consulta': 'Selecione a data e hora da consulta',
            'diagnostico': 'Descreva os sintomas, exames e diagnóstico',
            'prescricao': 'Medicamentos, dosagens, tratamentos e orientações',
        }