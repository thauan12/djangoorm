from django.contrib import admin
from core.models import Aluno, Boletim, Turma, Disciplina

@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'turno', 'disciplinasturma')

    def disciplinasturma(self,turma):
        return ', '.join(d.nome for d in turma.disciplina_set.all()[:2])

    disciplinasturma.short_description = 'Disciplinas'

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nomecompleto', 'dtnasc', 'endereco', 'turma')

    def nomecompleto(self, aluno):
        return f'{aluno.nome} {aluno.sobrenome}'

    nomecompleto.short_description= 'Nome'

@admin.register(Boletim)
class BoletimAdmin(admin.ModelAdmin):
    list_display = ('periodo', 'aluno')

@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'carga_horaria')

# Register your models here.
