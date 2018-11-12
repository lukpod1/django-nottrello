from django.shortcuts import render, redirect

from app.models import Tarefa, Projeto, Status, Usuario, Pergunta, Resposta
from .forms import CadastroForm, TarefaForm, ProjetoForm, EditarPerfilForm, PerguntaForm, RespostaForm
from .forms import EntrarForm
from django.core.paginator import Paginator, InvalidPage, EmptyPage




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
    data['usuario'] = Usuario.objects.get(pk=request.session['usuario_id'])
    return render(request, 'app/pergunta.html', data)

def forum(request):
    data = {}
    data['perguntas'] = Pergunta.objects.all()
    data['respostas'] = Resposta.objects.all()
    data['usuario'] = Usuario.objects.get(pk=request.session['usuario_id'])
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
        return redirect('/usuario/logado/')
    else:
        return redirect('/usuario/entrar')


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


def editarPerfil(request):
    data = {}
    data['usuario'] = Usuario.objects.get(pk=request.session['usuario_id'])
    data['formPerfil'] = EditarPerfilForm(
        request.POST or None, request.FILES or None, instance=data['usuario'])
    if data['formPerfil'].is_valid():
        data['formPerfil'].save()
        return redirect('/usuario/logado/')

    return render(request, 'app/formPerfil.html', data)


def usuarioLogado(request):
    data = {}
    data['projetos'] = Projeto.objects.filter(usuario=request.session['usuario_id'])
    data['usuario'] = Usuario.objects.get(pk=request.session['usuario_id'])
    formProjeto = ProjetoForm(request.POST or None)
    if formProjeto.is_valid():
        formProjeto.save()
        return redirect('/usuario/logado/')
    data['formProjeto'] = formProjeto
    formTarefa = TarefaForm(request.POST or None)
    if formTarefa.is_valid():
        formTarefa.save()
        return redirect('/usuario/logado/')
    data['formTarefa'] = formTarefa

    projetos = Projeto.objects.filter(usuario=request.session['usuario_id'])
    qtProjetoPendente = 0
    qtProjetoEmAndamento = 0
    qtProjetoConcluido = 0

    for projeto in projetos:
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


def listarTarefaProjeto(request, pk_projeto):
    data = {}
    # Tarefas filtradas por projeto
    tarefas = Tarefa.objects.filter(projeto=pk_projeto)
    # Projetos filtrados por usuario
    data['projetos'] = Projeto.objects.filter(usuario=request.session['usuario_id'])
    # Projeto específico
    data['projeto'] = Projeto.objects.get(pk=pk_projeto)
    #Usuario da sessão
    data['usuario'] = Usuario.objects.get(pk=request.session['usuario_id'])
    
    paginator = Paginator(tarefas, 10) # Mostra 10 tarefas por página
  
    # Esteja certo de que o `page request` é um inteiro. Se não, mostre a primeira página.
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    # Se o page request (9999) está fora da lista, mostre a última página.
    try:
        tarefas = paginator.page(page)
    except (EmptyPage, InvalidPage):
        tarefas = paginator.page(paginator.num_pages)

    data['tarefas'] = tarefas    

    formTarefa = TarefaForm(request.POST or None)
    if formTarefa.is_valid():
        formTarefa.save()
        return redirect('/projeto/' + str(pk_projeto))
    data['formTarefa'] = formTarefa
    formProjeto = ProjetoForm(request.POST or None)
    if formProjeto.is_valid():
        formProjeto.save()
        return redirect('/projeto/' + str(pk_projeto))
    data['formProjeto'] = formProjeto

    tarefas = Tarefa.objects.filter(projeto=pk_projeto)
    
    qtTarefaPendente = 0
    qtTarefaEmAndamento = 0
    qtTarefaConcluido = 0
    for tarefa in tarefas:
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
    data = {}
    data['projeto'] = Projeto.objects.get(pk=pk)
    form = ProjetoForm(request.POST or None, instance=data['projeto'])
    if form.is_valid():
        form.save()
        return redirect('/usuario/logado/')
    data['formProjeto'] = form    
    return render(request, 'app/formProjeto.html', data)


def excluirProjeto(request, pk):
    projeto = Projeto.objects.get(pk=pk)
    usuario = projeto.usuario.id
    projeto.delete()
    return redirect('/usuario/logado/')


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
    return redirect('/projeto/' + str(pk))

def editarTarefa(request, pk):
    data= {}
    tarefa = Tarefa.objects.get(pk=pk)
    data['projeto'] = Projeto.objects.get(pk=tarefa.projeto.id)
    form = TarefaForm(request.POST or None, instance=tarefa)
    if form.is_valid():
        form.save()
        return redirect('/projeto/' + str(tarefa.projeto.id))
    data['formTarefa'] = form
    return render(request, 'app/formTarefa.html', data)


def excluirTarefa(request, pk):
    tarefa = Tarefa.objects.get(pk=pk)
    tarefa.delete()
    return redirect('/projeto/' + str(tarefa.projeto.id))