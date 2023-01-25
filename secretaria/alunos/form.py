from django.forms import ModelForm
from .models import Aluno, Matricula, Mensalidade

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

class MatriculaForm(ModelForm):
    class Meta:
        model = Matricula
        fields = [
            'valor_mensal',
            'dia_vencimento'
        ]

