from django.shortcuts import render, redirect, get_object_or_404

from .forms import FormMostrarQuemPegou, FormMostrarQuemDevolveu
from .models import *


# Create your views here.
def home(request):
    return render(request, 'home.html')


def mostrar_chaves(request):
    list = Chave.objects.all()
    return render(request, 'mostrar_chaves.html',{'list':list})

def informacoes_chave(request, id):
    chave = Chave.objects.get(id=id)
    context = {
        'chave': chave
    }
    return render(request, 'informacoes_chave.html', context)

def mostrar_chaves_disponiveis(request):
    list = Chave.objects.filter(disponivel=True)
    return render(request, 'mostrar_chaves_disponiveis.html',{'list':list})

def mostrar_chaves_indisponiveis(request):
    list = Chave.objects.filter(disponivel=False)
    return render(request, 'mostrar_chaves_indisponiveis.html',{'list':list})

def pegar_chave(request, id):
    alterar = Chave.objects.filter(id=id).update(disponivel=False)
    list = Chave.objects.get(id=id)
    form = FormMostrarQuemPegou(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(home)
    return render(request, 'pegar_chave.html',{'form':form, 'list':list, 'alterar':alterar})

def devolver_chave(request, id):
    alterar = Chave.objects.filter(id=id).update(disponivel=True)
    list = Chave.objects.get(id=id)
    form = FormMostrarQuemDevolveu(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(home)
    return render(request, 'devolver_chave.html',{'form2':form, 'list2':list, 'alterar':alterar})

def historico_chave(request):
    list = Emprestimo.objects.all()
    list2 = Devolver.objects.all()
    return render(request, 'historico_chave.html',{'list': list, 'list2': list2})