from django.db import models

# Create your models here.
class Libros(models.Model):
    titulo = models.CharField(max_length=30)
    autor = models.CharField(max_length=30)
    genero = models.CharField(max_length=40)
    disponible = models.BooleanField(default=False)
    fecha = models.DateTimeField()
    cantidad = models.IntegerField()