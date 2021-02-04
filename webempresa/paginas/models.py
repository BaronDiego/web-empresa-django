from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Pagina(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = RichTextField()
    orden = models.SmallIntegerField(default=0)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['orden', 'titulo']

    def __str__(self):
        return self.titulo
