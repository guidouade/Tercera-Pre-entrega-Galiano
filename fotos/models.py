from django.db import models

# Create your models here.

class Categoria (models.Model):
    nombre=models.CharField(max_length = 60)

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__ (self):
        return self.nombre


class Post (models.Model):
    titulo=models.CharField(max_length = 60)
    contenido=models.CharField(max_length = 200)
    imagen=models.ImageField(upload_to='fotos', null=True, blank=True)
    categorias=models.ManyToManyField(Categoria)

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'

    def __str__ (self):
        return self.titulo