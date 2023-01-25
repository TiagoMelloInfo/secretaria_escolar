from django.contrib import admin
from .models import Aluno, Matricula, Mensalidade, Valores

admin.site.register((Aluno, Matricula, Mensalidade, Valores))

# Register your models here.
