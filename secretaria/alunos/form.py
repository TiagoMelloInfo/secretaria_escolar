from django.forms import ModelForm
from .models import Aluno

class AlunoForm(ModelForm):
    class Meta:
        model = Aluno
        fields = [
            'nome', 
            'sobrenome', 
            'nascimento'
        ]

class TelefoneForm(ModelForm):
    class Meta:
        model = Aluno
        fields = [
            'telefones'
        ]
