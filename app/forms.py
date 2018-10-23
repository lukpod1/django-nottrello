from django import forms

from .models import Usuario, Tarefa, Projeto


class CadastroForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('nome', 'email', 'senha')
        widgets = {
            'nome': forms.TextInput(
                attrs={'class': 'form-control', 'required': 'true',
                       'autofocus': 'true'}),
            'email': forms.EmailInput(
                attrs={'class': 'form-control', 'required': 'true',
                       'autofocus': 'true'}),

            'senha': forms.PasswordInput(
                attrs={'class': 'form-control', 'id': 'inputPassword', 'required': 'true'}),
        }


class EntrarForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('nome', 'senha')
        widgets = {
            'nome': forms.TextInput(
                attrs={'class': 'form-control', 'required': 'true', 'autofocus': 'true'}),
            'senha': forms.PasswordInput(
                attrs={'class': 'form-control', 'required': 'true'}),
        }


class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = {'nome', 'descricao', 'data_vencimento','projeto'}
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'data_vencimento': forms.DateInput(attrs={'placeholder': 'dd/mm/AAAA', 'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}),
            'projeto': forms.Select(attrs={'class': 'form-control'}),

        }

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = {'nome', 'data_vencimento'}
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'data_vencimento': forms.DateInput(attrs={'placeholder': 'dd/mm/AAAA', 'class': 'form-control'}),
        }