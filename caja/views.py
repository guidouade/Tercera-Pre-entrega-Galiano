from django.shortcuts import render
from caja.models import Caja, Categoria

# Create your views here.

def cajas (request):
    cajas = Caja.objects.all()
    return render (request, "caja/caja.html", {"cajas":cajas})

def categoria (request, categoria_id):
    categoria=Categoria.objects.get (id=categoria_id)
    cajas=Caja.objects.filter(categorias=categoria)
    return render (request, "caja/categoriacaja.html", {"categoria":categoria, "cajas":cajas})