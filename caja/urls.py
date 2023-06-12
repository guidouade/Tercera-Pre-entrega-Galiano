from django.urls import path
from . import views

urlpatterns = [
    path ('', views.cajas, name= "Caja de Recuerdos"),
    path ('categoria/<int:categoria_id>/', views.categoria, name= "categoria"),
]