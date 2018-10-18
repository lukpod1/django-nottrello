from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    
    return render(request, 'app/index.html')

def entrar(request):

    return render(request, 'app/formLogin.html')

def cadastrar(request):

    return render(request, 'app/formCadastro.html')

