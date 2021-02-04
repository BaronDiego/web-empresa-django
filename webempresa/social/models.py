from django.db import models
from django.db.models.fields import DateTimeField

# Create your models here.
class Link(models.Model):
    key = models.SlugField(verbose_name="Nombre clave", max_length=100, unique=True)
    nombre = models.CharField(verbose_name="Red Social", max_length=200)
    url = models.URLField(verbose_name="Enlace", max_length=200, null=True, blank=True)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "enlace"
        verbose_name_plural = "enlaces"
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre