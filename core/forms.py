from django import forms
from .models import Chave, Usuario, Emprestimo, Devolver


class FormCadastroChave(forms.ModelForm):

    class Meta:

        model = Chave
        fields = ['nome', 'disponivel']

class FormCadastroUsuario(forms.ModelForm):

    class Meta:

        model = Usuario
        fields = ['nome', 'cargo']

class FormMostrarQuemPegou(forms.ModelForm):

    class Meta:

        model = Emprestimo
        fields = ['nome', 'chave', 'horas_pegou']

class FormMostrarQuemDevolveu(forms.ModelForm):

    class Meta:

        model = Devolver
        fields = ['nome', 'chave', 'horas_devolveu']