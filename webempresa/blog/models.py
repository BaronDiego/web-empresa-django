from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    creado = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    actualizado = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        ordering = ["-creado"]

    def __str__(self):
        return self.nombre

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    publicado = models.DateTimeField(verbose_name="Fecha de publicación", default=now)
    imagen = models.ImageField(upload_to="blog", null=True, blank=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    categorias = models.ManyToManyField(Categoria, related_name="get_post")
    creado = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    actualizado = models.DateTimeField(auto_now=True, verbose_name="Fecha de actulización")

    class Meta:
        verbose_name = "entrada"
        verbose_name_plural = "entradas"
        ordering = ["-creado"]

    def __str__(self):
        return self.titulo