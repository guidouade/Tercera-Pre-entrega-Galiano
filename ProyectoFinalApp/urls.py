from django.urls import path
from ProyectoFinalApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path ('', views.inicio, name= "Inicio"),
    path ('relatos/', views.relatoshistoricos, name= "Relatos Históricos"),
    path ('videos/', views.videos, name= "Videos"),
    path ('busqueda_recuerdos/', views.busqueda_recuerdos),
    path ('buscar_recuerdo/', views.buscar_recuerdo),
    path ('busqueda_fototecas/', views.busqueda_fototecas),
    path ('buscar/', views.buscar),

]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)