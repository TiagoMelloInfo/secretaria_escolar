from django.db import models

class Aluno(models.Model):
    aluno_id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)
    nascimento = models.DateField()
    telefones = models.TextField()
    enderecos = models.TextField()
    responsavel = models.TextField()

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'

class Matricula(models.Model):
    matricula_id = models.AutoField(primary_key=True)
    aluno_id = models.ForeignKey('Aluno', on_delete=models.CASCADE)
    data_matricula = models.DateTimeField()
    ano_vigencia = models.IntegerField()
    dia_vencimento = models.IntegerField()
    mensalidade_id = models.ForeignKey('Valores', on_delete=models.CASCADE)
    bolsa_desconto = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.matricula_id}'

class Mensalidade(models.Model):
    mensalidade_id = models.AutoField(primary_key=True)
    matricula_id = models.ForeignKey('Matricula', on_delete=models.CASCADE)
    mes_vigencia = models.IntegerField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.mensalidade_id} - {self.matricula_id}'

class Valores(models.Model):
    valores_id = models.AutoField(primary_key=True)
    ano_vigencia = models.IntegerField()
    ano_escolar = models.TextField()
    valor = models.IntegerField()

    def __str__(self):
        return f'Ano: {self.ano_vigencia} | Serie: {self.ano_escolar} | Valor: {self.valor}'
