from ast import AugStore
from multiprocessing.dummy import current_process
from django.db import models
# Create your models here.

class BlogModel(models.Model):
    titulo = models.CharField(max_length=100) 
    subtitulo= models.CharField(max_length=100)
    descripcion= models.CharField(max_length=100)
    cuerpo = models.TextField()
    autor = models.CharField(max_length=100)
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nombre