from django.contrib import admin
from .models import Libros


class LibrosAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'autor', 'genero', 'disponible', 'fecha', 'cantidad']

admin.site.register(Libros, LibrosAdmin)