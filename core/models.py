from django.db import models

# Create your models here.
class Turma(models.Model):
    turnos = (
        ('matutino', 'Matutino'),
        ('vespertino', 'Vespertino'),
        ('noturno', 'Noturno'),
    )
    nome = models.CharField('Nome',max_length=50)
    turno = models.CharField('Turno', choices=turnos, max_length=10)

    def __str__(self):
        return self.nome

class Aluno(models.Model):
    nome = models.CharField('Nome', max_length=50)
    sobrenome = models.CharField('Sobrenome', max_length=70)
    endereco = models.CharField('Endereço', max_length=100)
    dtnasc = models.DateField('Data de nascimento')
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE, related_name='alunos_turma')

    class Meta:
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'

class Boletim(models.Model):
    periodo = models.PositiveIntegerField('Periodo')
    aluno = models.OneToOneField(Aluno, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Boletim'
        verbose_name_plural = 'Boletins'

    def __str__(self):
        return f'Boletim do aluno {self.aluno.nome}'

class Disciplina(models.Model):
    carga_horaria = models.PositiveIntegerField('Carga Horaria')
    nome = models.CharField('Nome', max_length=50)
    descricao = models.TextField('Descrição')
    turma = models.ManyToManyField(Turma)

    class Meta:
        verbose_name = 'Disciplina'
        verbose_name_plural = 'Disciplinas'

    def __str__(self):
        return self.nome