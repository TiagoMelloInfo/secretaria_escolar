import json

from django.shortcuts import render, redirect, get_object_or_404
from utils.payloader import Payloader

from .models import Aluno

payloader = Payloader()

def home(request):
    payload = payloader.res()
    payload['titulo'] = 'Aluno'
    payload['alunos'] = Aluno.objects.all()

    return render(request, 'index.html', payload)

def cadastro_aluno(request, id: int):
    payload = payloader.res()
    payload['titulo'] = 'Aluno X'
    payload['aluno'] = get_object_or_404(Aluno, pk=id)
    payload['idade'] = int((payload['hoje'] - payload['aluno'].nascimento).days / 365)

    payload['aluno'].telefones = json.loads(payload['aluno'].telefones)
    payload['aluno'].enderecos = json.loads(payload['aluno'].enderecos)
    payload['aluno'].responsavel = json.loads(payload['aluno'].responsavel)

    return render(request, 'cadastro_aluno.html', payload)

def novo_aluno(request):
    payload = payloader.res()
    payload['titulo'] = 'Novo Aluno'
    form = request.POST

    aluno = Aluno()

    aluno.nome = nome = form.get('nome', '').title()
    aluno.sobrenome = sobrenome = form.get('sobrenome', '').title()
    aluno.nascimento = nascimento = form.get('nascimento')

    if nome and sobrenome and nascimento:
        aluno.telefones = json.dumps([])
        aluno.enderecos = json.dumps([])
        aluno.responsavel = json.dumps([])
        aluno.save()
        return redirect('alunos_home')
    return render(request, 'novo_aluno.html', payload)

def novo_telefone(request, id: int):
    payload = payloader.res()
    payload['titulo'] = 'Novo Telefone'
    payload['aluno'] = aluno = get_object_or_404(Aluno, pk=id)

    form = request.POST

    telefone = {}
    telefone['ddd'] = form.get('ddd', '')
    telefone['telefone'] = form.get('telefone', '')
    telefone['is_whatsapp'] = {'on': True}.get(form.get('is_whatsapp', ''), False)

    if form:
            telefones = payload['aluno'].telefones
            telefones = json.loads(telefones)
            telefones.append(telefone)
            aluno.telefones = json.dumps(telefones)
            aluno.save()
            print('salvo')
            return redirect('alunos_home')
    return render(request, 'novo_telefone.html', payload)
