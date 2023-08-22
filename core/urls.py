from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('criarTurma/', views.TurmaCreateView.as_view(), name='criarTurma'),
    path('criarAluno/', views.AlunoCreateView.as_view(), name='criarAluno'),

]