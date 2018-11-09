from django.shortcuts import render, redirect

from app.models import Tarefa, Projeto, Status, Usuario, Pergunta, Resposta
from .forms import CadastroForm, TarefaForm, ProjetoForm, EditarPerfilForm, PerguntaForm, RespostaForm
from .forms import EntrarForm

import json


# Create your views here.
def home(request):
    return render(request, 'app/index.html')


def entrar(request):
    form = EntrarForm(request.POST or None)
    if form.is_valid():
        return logar(request)

    return render(request, 'app/formLogin.html', {'formLogin': form})


def pergunta(request, pk):
    data= {}
    data['pergunta'] = Pergunta.objects.get(pk=pk)
    data['respostas'] = Resposta.objects.filter(pergunta=pk)
    return render(request, 'app/pergunta.html', data)

def forum(request):
    data = {}
    data['perguntas'] = Pergunta.objects.all()
    data['respostas'] = Resposta.objects.all()
    form = PerguntaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/forum')
    data['formPergunta'] = form
    return render(request, 'app/forum.html', data)

def responderPergunta(request, pk):
    form = RespostaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/forum/pergunta/' + str(pk))
    return render(request, 'app/responderPergunta.html', {'formResposta': form})


def logar(request):
    usuarioLogado = Usuario.objects.get(nomeUsuario=request.POST['nomeUsuario'])
    if usuarioLogado.senha == request.POST['senha']:
        request.session['usuario_id'] = usuarioLogado.id
        return redirect('/usuario/logado/' + str(usuarioLogado.id))
    else:
        return redirect('usuario/entrar')


def logout(request):
    try:
        del request.session['usuario_id']
    except KeyError:
        pass
    return redirect('/usuario/entrar')


def cadastrar(request):
    form = CadastroForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/usuario/entrar')

    return render(request, 'app/formCadastro.html', {'formCadastro': form})


def editarPerfil(request, pk_usuario):
    data = {}
    data['usuario'] = Usuario.objects.get(pk=pk_usuario)
    data['formPerfil'] = EditarPerfilForm(
        request.POST or None, request.FILES or None, instance=data['usuario'])
    if data['formPerfil'].is_valid():
        data['formPerfil'].save()
        return redirect('/usuario/logado/'+str(pk_usuario))

    return render(request, 'app/formPerfil.html', data)


def usuarioLogado(request, pk_usuario):
    data = {}
    data['projetos'] = Projeto.objects.filter(usuario=pk_usuario)
    data['usuario'] = Usuario.objects.get(pk=pk_usuario)
    formProjeto = ProjetoForm(request.POST or None)
    if formProjeto.is_valid():
        formProjeto.save()
        return redirect('/usuario/logado/'+str(pk_usuario))
    data['formProjeto'] = formProjeto

    queryset = Projeto.objects.filter(usuario=pk_usuario)
    qtProjetoPendente = 0
    qtProjetoEmAndamento = 0
    qtProjetoConcluido = 0

    for projeto in queryset:
        if (projeto.status.id == 1):
            qtProjetoPendente += 1
            data['qtPendente'] = qtProjetoPendente
        if (projeto.status.id == 2):
            qtProjetoEmAndamento += 1
            data['qtEmAndamento'] = qtProjetoEmAndamento
        if (projeto.status.id == 3):
            qtProjetoConcluido += 1
            data['qtConcluido'] = qtProjetoConcluido
    return render(request, 'app/usuarioLogado.html', data)


def listarTarefaProjeto(request, pk_usuario, pk_projeto):
    data = {}
    # Tarefas filtradas por projeto
    data['tarefas'] = Tarefa.objects.filter(projeto=pk_projeto)
    # Projetos filtrados por usuario
    data['projetos'] = Projeto.objects.filter(usuario=pk_usuario)
    # Projeto específico
    data['projeto'] = Projeto.objects.get(pk=pk_projeto)

    formTarefa = TarefaForm(request.POST or None)
    if formTarefa.is_valid():
        formTarefa.save()
        return redirect('/'+str(pk_usuario)+'/projeto/' + str(pk_projeto))
    data['formTarefa'] = formTarefa
    formProjeto = ProjetoForm(request.POST or None)
    if formProjeto.is_valid():
        formProjeto.save()
        return redirect('/' + str(pk_usuario)+'/projeto/' + str(pk_projeto))
    data['formProjeto'] = formProjeto

    queryset = Tarefa.objects.filter(projeto=pk_projeto)
    qtTarefaPendente = 0
    qtTarefaEmAndamento = 0
    qtTarefaConcluido = 0


    for tarefa in queryset:
        if (tarefa.status.id == 1):
            qtTarefaPendente += 1
            data['qtPendente'] = qtTarefaPendente
        elif (tarefa.status.id == 2):
            qtTarefaEmAndamento += 1
            data['qtEmAndamento'] = qtTarefaEmAndamento
        elif (tarefa.status.id == 3):
            qtTarefaConcluido += 1
            data['qtConcluido'] = qtTarefaConcluido

    return render(request, 'app/listaTarefa.html', data)


def editarProjeto(request, pk):
    projeto = Projeto.objects.get(pk=pk)
    form = ProjetoForm(request.POST or None, instance=projeto)
    if form.is_valid():
        form.save()
        return redirect('/usuario/logado/'+str(projeto.usuario.id))
    return render(request, 'app/formProjeto.html', {'formProjeto': form})


def excluirProjeto(request, pk):
    projeto = Projeto.objects.get(pk=pk)
    usuario = projeto.usuario.id
    projeto.delete()
    return redirect('/usuario/logado/'+str(projeto.usuario.id))


def concluirProjeto(request, pk):
    projeto = Projeto.objects.get(pk=pk)
    usuario = projeto.usuario_id
    status = Status.objects.get(pk=3)
    tarefas = Tarefa.objects.filter(projeto=pk)
    for tarefa in tarefas:
        if tarefa.status.id != 3:
            tarefa.status = status
            tarefa.save()
        projeto.status = status
        projeto.save()
    return redirect('/' + str(usuario)+'/projeto/' + str(pk))

def editarTarefa(request, pk):
    tarefa = Tarefa.objects.get(pk=pk)
    form = TarefaForm(request.POST or None, instance=tarefa)
    if form.is_valid():
        form.save()
        return redirect('/'+str(tarefa.projeto.usuario.id)+'/projeto/' + str(tarefa.projeto.id))
    return render(request, 'app/formTarefa.html', {'formTarefa': form})


def excluirTarefa(request, pk):
    tarefa = Tarefa.objects.get(pk=pk)
    tarefa.delete()
    return redirect('/'+str(tarefa.projeto.usuario.id)+'/projeto/' + str(tarefa.projeto.id))