from django import forms

from .models import Usuario, Tarefa


class CadastroForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('nome', 'email', 'senha')
        widgets = {
            'senha': forms.PasswordInput(),
        }


class EntrarForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('nome', 'senha')
        widgets = {
            'senha': forms.PasswordInput(),
        }

class TarefaForm(forms.ModelForm, forms.Form):
    class Meta:
        model = Tarefa
        fields = {'nome', 'descricao', 'data_vencimento'}
        widgets = {
            'data_vencimento': forms.DateInput(attrs={'placeholder': 'dd/mm/AAAA'}), 'descricao': forms.Textarea(),

        }