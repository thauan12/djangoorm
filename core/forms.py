from django import forms

from core.models import Turma, Aluno


class AddTurmaForm(forms.ModelForm):
    class Meta:
        model = Turma
        fields = ['nome', 'turno']

class AddAlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome','sobrenome','endereco','dtnasc','turma']