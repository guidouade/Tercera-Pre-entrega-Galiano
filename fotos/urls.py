from django.urls import path
from . import views

urlpatterns = [
    path ('', views.fotos, name= "Fototeca"),
    path ('categoria/<int:categoria_id>/', views.categoria, name= "categoria"),
]