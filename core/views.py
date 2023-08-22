from django.shortcuts import render
from django.template.context_processors import request
from django.views.generic import ListView, TemplateView, DetailView, FormView, CreateView
from core.models import Turma, Aluno
from core.forms import AddTurmaForm, AddAlunoForm
from django.shortcuts import render, redirect


class IndexView(TemplateView):
    template_name = "index.html"

class TurmaCreateView(CreateView):
    model = Turma
    form_class = AddTurmaForm
    template_name = 'turmaCad.html'
    success_url = '/criarTurma/'

class AlunoCreateView(CreateView):
    model = Aluno
    form_class = AddAlunoForm
    template_name = 'alunoCad.html'
    success_url = '/criarAluno/'