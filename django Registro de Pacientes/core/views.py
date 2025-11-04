from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login, logout
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from io import BytesIO
import datetime
from .models import Paciente, Atendimento
from .forms import PacienteForm, AtendimentoForm, UserRegisterForm
from django.utils import timezone
from .models import Matricula

# View da página inicial
def home(request):
    return render(request, 'index.html')

# Views de autenticação
def register(request):
    # Obter matrículas disponíveis para mostrar no template
    matriculas_disponiveis = Matricula.objects.filter(disponivel=True)
    
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Conta criada com sucesso! Bem-vindo ao sistema.')
            return redirect('lista_pacientes')
    else:
        form = UserRegisterForm()
    
    return render(request, 'registration/register.html', {
        'form': form,
        'matriculas_disponiveis': matriculas_disponiveis
    })

def custom_logout(request):
    logout(request)
    messages.info(request, 'Você saiu do sistema com sucesso.')
    return redirect('home')

# Views de pacientes
@login_required
def lista_pacientes(request):
    pacientes = Paciente.objects.all().order_by('nome')
    return render(request, 'pacientes/lista.html', {'pacientes': pacientes})

@login_required
def novo_paciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Paciente cadastrado com sucesso!')
            return redirect('lista_pacientes')
    else:
        form = PacienteForm()
    return render(request, 'pacientes/form.html', {'form': form, 'titulo': 'Novo Paciente'})

@login_required
def editar_paciente(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)
    if request.method == 'POST':
        form = PacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
            messages.success(request, 'Paciente atualizado com sucesso!')
            return redirect('lista_pacientes')
    else:
        form = PacienteForm(instance=paciente)
    return render(request, 'pacientes/form.html', {'form': form, 'titulo': 'Editar Paciente'})

@login_required
def excluir_paciente(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)
    if request.method == 'POST':
        paciente.delete()
        messages.success(request, 'Paciente excluído com sucesso!')
        return redirect('lista_pacientes')
    return render(request, 'pacientes/confirmar_exclusao.html', {'paciente': paciente})

# Views de atendimentos
@login_required
def lista_atendimentos(request):
    atendimentos = Atendimento.objects.all().order_by('-data_consulta')
    return render(request, 'atendimentos/lista.html', {'atendimentos': atendimentos})

@login_required
def novo_atendimento(request):
    paciente_id = request.GET.get('paciente')
    paciente_inicial = None
    
    if paciente_id:
        paciente_inicial = get_object_or_404(Paciente, id=paciente_id)
    
    if request.method == 'POST':
        form = AtendimentoForm(request.POST)
        if form.is_valid():
            atendimento = form.save()
            messages.success(request, f'Consulta registrada para {atendimento.paciente.nome}')
            return redirect('lista_atendimentos')
    else:
        initial = {}
        if paciente_inicial:
            initial['paciente'] = paciente_inicial
        form = AtendimentoForm(initial=initial)
    
    return render(request, 'atendimentos/form.html', {
        'form': form, 
        'titulo': 'Nova Consulta',
        'paciente_inicial': paciente_inicial
    })

@login_required
def editar_atendimento(request, atendimento_id):
    atendimento = get_object_or_404(Atendimento, id=atendimento_id)
    if request.method == 'POST':
        form = AtendimentoForm(request.POST, instance=atendimento)
        if form.is_valid():
            form.save()
            messages.success(request, 'Consulta atualizada com sucesso!')
            return redirect('lista_atendimentos')
    else:
        form = AtendimentoForm(instance=atendimento)
    return render(request, 'atendimentos/form.html', {'form': form, 'titulo': 'Editar Consulta'})

@login_required
def excluir_atendimento(request, atendimento_id):
    atendimento = get_object_or_404(Atendimento, id=atendimento_id)
    if request.method == 'POST':
        paciente_nome = atendimento.paciente.nome
        atendimento.delete()
        messages.success(request, f'Consulta de {paciente_nome} excluída com sucesso!')
        return redirect('lista_atendimentos')
    return render(request, 'atendimentos/confirmar_exclusao.html', {'atendimento': atendimento})

# Views de relatórios
@login_required
def relatorios(request):
    total_pacientes = Paciente.objects.count()
    total_atendimentos = Atendimento.objects.count()
    return render(request, 'relatorios.html', {
        'total_pacientes': total_pacientes,
        'total_atendimentos': total_atendimentos,
    })

@login_required
def relatorio_pdf(request):
    # Criar um buffer para o PDF
    buffer = BytesIO()
    
    # Criar o objeto canvas
    p = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter
    
    # Configurar o título
    p.setFont("Helvetica-Bold", 16)
    p.drawString(1 * inch, height - 1 * inch, "Relatório de Atendimentos - Sistema de Pacientes")
    
    # Data de geração
    p.setFont("Helvetica", 10)
    p.drawString(1 * inch, height - 1.3 * inch, f"Gerado em: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M')}")
    
    # Estatísticas
    total_pacientes = Paciente.objects.count()
    total_atendimentos = Atendimento.objects.count()
    
    p.drawString(1 * inch, height - 1.6 * inch, f"Total de Pacientes: {total_pacientes}")
    p.drawString(1 * inch, height - 1.8 * inch, f"Total de Atendimentos: {total_atendimentos}")
    
    # Lista de atendimentos
    y_position = height - 2.5 * inch
    p.setFont("Helvetica-Bold", 12)
    p.drawString(1 * inch, y_position, "Últimos Atendimentos:")
    
    atendimentos = Atendimento.objects.all().order_by('-data_consulta')[:10]
    p.setFont("Helvetica", 10)
    
    for atendimento in atendimentos:
        y_position -= 0.25 * inch
        if y_position < 1 * inch:  # Nova página se necessário
            p.showPage()
            y_position = height - 1 * inch
            p.setFont("Helvetica", 10)
        
        linha = f"{atendimento.data_consulta.strftime('%d/%m/%Y')} - {atendimento.paciente.nome} - {atendimento.diagnostico[:50]}..."
        p.drawString(1 * inch, y_position, linha)
    
    # Finalizar o PDF
    p.showPage()
    p.save()
    
    # Obter o valor do buffer
    buffer.seek(0)
    
    # Criar a resposta HTTP
    response = HttpResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="relatorio_atendimentos.pdf"'
    
    return response