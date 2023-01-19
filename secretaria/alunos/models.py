from django.db import models

class Aluno(models.Model):
    aluno_id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)
    nascimento = models.DateField()
    telefones = models.TextField()
    enderecos = models.TextField()
    responsavel = models.TextField()
