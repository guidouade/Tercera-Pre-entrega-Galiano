from django.shortcuts import render
from .forms import FormularioSugerencias
from .models import Sugerencia

# Create your views here.

def sugerencia (request):
      if request.method == 'POST':
            miFormulario = FormularioSugerencias(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
            if miFormulario.is_valid():
                  informacion = miFormulario.cleaned_data
                  sugerir= Sugerencia(nombre=informacion['nombre'], email=informacion['email'], sugerencia=informacion['sugerencia'])
                  sugerir.save()
                  return render(request, "ProyectoFinalApp/inicio.html")
      else:
            miFormulario = FormularioSugerencias()
      return render(request,"sugerencia/miFormulario.html", {"miFormulario":miFormulario})