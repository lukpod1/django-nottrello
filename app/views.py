from django.shortcuts import render, redirect

from app.models import Tarefa, Projeto, Status
from .forms import CadastroForm, TarefaForm
from .forms import EntrarForm


# Create your views here.
def home(request):
    return render(request, 'app/index.html')


def entrar(request):
    form = EntrarForm(request.POST or None)
    if form.is_valid():
        return redirect('/usuario/logado')

    return render(request, 'app/formLogin.html', {'formLogin': form})


def cadastrar(request):
    form = CadastroForm(request.POST or None)
    if form.is_valid():
        form.save()
        return entrar(request)

    return render(request, 'app/formCadastro.html', {'formCadastro': form})


def usuarioLogado(request):
    data = {}
    data['tarefas'] = Tarefa.objects.all()
    data['projetos'] = Projeto.objects.all()
    form = TarefaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/usuario/logado')
    data['formTarefa'] = form

    return render(request, 'app/usuarioLogado.html', data)


# def adicionarTarefa(request):
#     form = TarefaForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect('/usuario/logado')
#     return render(request, 'app/testemodal.html', {'formTarefa': form})


def editarTarefa(request, pk):
    tarefa = Tarefa.objects.get(pk=pk)
    form = TarefaForm(request.POST or None, instance=tarefa)
    if form.is_valid():
        form.save()
        return redirect('/usuario/logado')
    return render(request, 'app/formTarefa.html', {'formTarefa': form})

def excluirTarefa(request, pk):
    tarefa = Tarefa.objects.get(pk=pk)
    tarefa.delete()
    return redirect('/usuario/logado')



def marcarConcluido(request, pk):
    tarefa = Tarefa.objects.get(pk=pk)
    status = Status(Status.objects.filter(id=3))

    tarefa.status=status
    tarefa.save()




