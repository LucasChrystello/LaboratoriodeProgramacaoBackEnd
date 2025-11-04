from django.db import models
from django.contrib.auth.models import User

class Matricula(models.Model):
    numero = models.CharField(max_length=20, unique=True, verbose_name="Número da Matrícula")
    disponivel = models.BooleanField(default=True, verbose_name="Disponível para uso")
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_utilizacao = models.DateTimeField(null=True, blank=True)
    usuario = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='matricula_usuario')

    def __str__(self):
        status = "Disponível" if self.disponivel else f"Usada por: {self.usuario.username}"
        return f"Matrícula {self.numero} - {status}"

    class Meta:
        verbose_name = "Matrícula"
        verbose_name_plural = "Matrículas"

class Paciente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20)
    data_nascimento = models.DateField()
    endereco = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

class Atendimento(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    data_consulta = models.DateTimeField()
    diagnostico = models.TextField()
    prescricao = models.TextField()
    
    def __str__(self):
        return f"Consulta {self.paciente.nome} - {self.data_consulta}"