from django import forms

from .models import Usuario, Tarefa, Projeto, Pergunta, Resposta


class CadastroForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('nomeCompleto', 'nomeUsuario', 'email', 'senha')
        widgets = {

            'nomeCompleto': forms.TextInput(
                attrs={'class': 'form-control', 'required': 'true',
                       'autofocus': 'true'}),
            'nomeUsuario': forms.TextInput(
                attrs={'class': 'form-control', 'required': 'true'}),
            'email': forms.EmailInput(
                attrs={'class': 'form-control', 'required': 'true'}),

            'senha': forms.PasswordInput(
                attrs={'class': 'form-control', 'id': 'inputPassword', 'required': 'true'}),
        }


class EditarPerfilForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('nomeCompleto', 'nomeUsuario', 'senha', 'avatar')
        widgets = {
            'nomeCompleto': forms.TextInput(
                attrs={'class': 'form-control', 'required': 'true',
                       'autofocus': 'true'}),
            'nomeUsuario': forms.TextInput(
                attrs={'class': 'form-control', 'required': 'true'}),
            'senha': forms.TextInput(
                attrs={'class': 'form-control', 'type':'password'}),
            'avatar': forms.FileInput(attrs={'class': 'form-control'}),
        }


class EntrarForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('nomeUsuario', 'senha')
        widgets = {
            'nomeUsuario': forms.TextInput(
                attrs={'class': 'form-control', 'required': 'true', 'autofocus': 'true'}),
            'senha': forms.PasswordInput(
                attrs={'class': 'form-control', 'required': 'true'}),
        }


class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = {'id', 'nome', 'descricao', 'data_vencimento','status', 'projeto'}
        widgets = {
            'id': forms.NumberInput(attrs={'id': 'id'}),
            'nome': forms.TextInput(attrs={'class': 'form-control', 'id': 'nome'}),
            'data_vencimento': forms.DateInput(attrs={'placeholder': 'dd/mm/AAAA', 'class': 'form-control', 'id': 'data_vencimento'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}),
            'status' : forms.Select(attrs={'class': 'form-control'}),
            'projeto' : forms.Select(attrs={'class': 'form-control'}),

        }


class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = {'nome', 'data_vencimento', 'detalhes', 'usuario', 'status'}
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'id': 'nome'}),
            'data_vencimento': forms.DateInput(attrs={'placeholder': 'dd/mm/AAAA', 'class': 'form-control', 'id': 'data_vencimento'}),
            'detalhes': forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}),
            'usuario':forms.HiddenInput(attrs={'class':'form-control', }),
            'status' : forms.Select(attrs={'class': 'form-control'}),

        }

class PerguntaForm(forms.ModelForm):
    class Meta:
        model = Pergunta   
        fields = {'titulo','detalhesPergunta', 'usuario'}
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'id': 'titulo'}),            
            'detalhesPergunta': forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}),


        }     


class RespostaForm(forms.ModelForm):
    class Meta:
        model = Resposta  
        fields = {'conteudo', 'usuario', 'pergunta'}
        widgets = {
            'conteudo': forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}), 
            'usuario': forms.Select(attrs={'class': 'form-control' }),  
            'pergunta': forms.Select(attrs={'class': 'form-control'}),   
                   
           
        }           
