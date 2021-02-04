from django.contrib import admin
from django.db import models
from .models import Categoria, Post

# Register your models here.
class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields = ("creado", "actualizado")

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ("creado", "actualizado")
    list_display = ('titulo', 'autor','publicado', 'post_categorias')
    ordering = ('autor', 'publicado')
    search_fields = ('titulo', 'contenido','autor__username', 'categorias__nombre')
    date_hierarchy = 'publicado'
    list_filter = ('autor__username', 'categorias__nombre')

    def post_categorias(self, obj):
        return ", ".join([c.nombre for c in obj.categorias.all().order_by("nombre")])
    post_categorias.short_description = "Categorias"

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Post, PostAdmin)
