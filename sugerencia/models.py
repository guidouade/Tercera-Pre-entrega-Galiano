from django.db import models

# Create your models here.

from django.db import models

# Create your models here.

class Sugerencia (models.Model):
    nombre= models.CharField(max_length=200)
    email= models.EmailField(max_length=200)
    sugerencia= models.CharField(max_length=2000)

    class Meta:
        verbose_name = 'sugerencia'
        verbose_name_plural = 'sugerencias'

    def __str__ (self):
        return self.sugerencia