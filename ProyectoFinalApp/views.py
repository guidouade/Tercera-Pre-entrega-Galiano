from django.shortcuts import render, HttpResponse
from fotos.models import Post
from caja.models import Caja

# Create your views here.

def inicio (request):
    return render (request, "ProyectoFinalApp/inicio.html")

def relatoshistoricos (request):
    return render (request, "ProyectoFinalApp/relatos.html")

def videos (request):
    return render (request, "ProyectoFinalApp/videos.html")

def busqueda_fototecas (request):
    return render (request, "fotos/busqueda_fototecas.html")

def buscar (request):
    if request.GET["fttc"]:
        mensaje= "Fototeca buscada: %r" %request.GET["fttc"]
        fototeca=request.GET["fttc"]
        fotos=Post.objects.filter (titulo__icontains=fototeca)
        return render (request, "fotos/resultados_busqueda.html", {"fotos":fotos, "query":fototeca})
    else:
        mensaje="No introdujiste nada"

    return HttpResponse(mensaje)

def busqueda_recuerdos (request):
    return render (request, "caja/busqueda_recuerdos.html")

def buscar_recuerdo (request):
    if request.GET["fttc"]:
        mensaje= "Recuerdo buscado: %r" %request.GET["fttc"]
        caja=request.GET["fttc"]
        recuerdos=Caja.objects.filter (titulo__icontains=caja)
        return render (request, "caja/resultados_busqueda.html", {"recuerdos":recuerdos, "query":caja})
    else:
        mensaje="No introdujiste nada"

    return HttpResponse(mensaje)