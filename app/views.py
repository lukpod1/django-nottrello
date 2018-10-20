from django.shortcuts import render, redirect

from app.models import Tarefa, Projeto
from .forms import CadastroForm
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
    return render(request, 'app/usuarioLogado.html', data)