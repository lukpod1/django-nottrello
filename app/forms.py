from django import forms

from .models import Usuario

class CadastroForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('nome', 'email', 'senha')


class EntrarForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('nome', 'senha')