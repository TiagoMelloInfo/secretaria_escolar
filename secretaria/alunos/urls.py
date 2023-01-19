from django.urls import path

from .views import (
    home,
    novo_aluno,
    cadastro_aluno,
    novo_telefone,
    )

urlpatterns = [
    path('', home, name='alunos_home'),
    path('novo/', novo_aluno, name='novo_aluno'),
    path('consulta/<int:id>', cadastro_aluno, name='consulta_aluno'),
    path('novo-telefone/<int:id>', novo_telefone, name='novo_telefone'),
]
