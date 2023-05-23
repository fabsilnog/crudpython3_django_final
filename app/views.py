from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.http import HttpResponse
from app.forms import ProdutoForm
from app.models import Produto
from io import BytesIO
from django.http import HttpResponse



# Create your views here.

def home(request):
    data = {}
    data['db'] = Produto.objects.all()
    return render(request, 'index.html', data)

def fechapedido(request):
        data = {}
        data['db'] = Produto.objects.all()
        return render(request, 'fechapedido.html', data)

def form(request):
    data = {}
    data['form'] = ProdutoForm()
    return render(request, 'form.html', data)

def create(request):
    form = ProdutoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def view(request, pk):
    data = {}
    data['db'] = Produto.objects.get(pk=pk)
    return render(request, 'view.html', data)

def edit(request, pk):
    data = {}
    data['db'] = Produto.objects.get(pk=pk)
    data['form'] = ProdutoForm(instance=data['db'])
    return render(request, 'form.html', data)

def update(request, pk):
    data = {}
    data['db'] = Produto.objects.get(pk=pk)
    form = ProdutoForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')

def delete(request, pk):
    db = Produto.objects.get(pk=pk)
    db.delete()
    return redirect('home')
