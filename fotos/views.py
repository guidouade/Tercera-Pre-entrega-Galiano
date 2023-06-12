from django.shortcuts import render
from fotos.models import Post, Categoria

# Create your views here.

def fotos (request):
    posts = Post.objects.all()
    return render (request, "fotos/fototeca.html", {"posts":posts})

def categoria (request, categoria_id):
    categoria=Categoria.objects.get (id=categoria_id)
    posts = Post.objects.filter(categorias=categoria)
    return render (request, "fotos/categoria.html", {"categoria":categoria, "posts":posts})
    