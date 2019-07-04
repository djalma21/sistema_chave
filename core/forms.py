from django import forms
from .models import Chave, Emprestimo, Devolver


class FormCadastroChave(forms.ModelForm):

    class Meta:

        model = Chave
        fields = ['nome', 'disponivel']

class FormMostrarQuemPegou(forms.ModelForm):

    class Meta:

        model = Emprestimo
        fields = ['user', 'chave', 'horas_pegou']

class FormMostrarQuemDevolveu(forms.ModelForm):

    class Meta:

        model = Devolver
        fields = ['user', 'chave', 'horas_devolveu']