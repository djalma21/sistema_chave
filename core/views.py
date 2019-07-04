from django.shortcuts import render, redirect, get_object_or_404

from .forms import FormMostrarQuemPegou, FormMostrarQuemDevolveu
from .models import *
from django.contrib.auth.decorators import login_required



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

@login_required
def pegar_chave(request, id):
    list = Chave.objects.filter
    form = FormMostrarQuemPegou(request.POST or None)
    if form.is_valid():
        alterar = Chave.objects.filter(id=id).update(disponivel=False)
        form.save()
        return redirect(home)
    return render(request, 'pegar_chave.html',{'form':form, 'list':list})

@login_required
def devolver_chave(request,id):
    list2 = Emprestimo.objects.filter(user=request.user.id)
    form = FormMostrarQuemDevolveu(request.POST or None)
    if form.is_valid():
        alterar = Chave.objects.filter(id=id).update(disponivel=True)
        form.save()
        return redirect(home)
    return render(request, 'devolver_chave.html',{'form2':form, 'list2':list2})

def historico_chave(request):
    list = Emprestimo.objects.filter(user=request.user.id)
    list2 = Devolver.objects.filter(user=request.user.id)
    return render(request, 'historico_chave.html',{'list': list, 'list2': list2})