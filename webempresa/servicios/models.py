from django.db import models

# Create your models here.

class Servicio(models.Model):
    titulo = models.CharField(max_length=200)
    sub_titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to="servicios")
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-creado"]

    def __str__(self):
        return self.titulo
