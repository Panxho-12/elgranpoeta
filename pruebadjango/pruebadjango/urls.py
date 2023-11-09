from django.contrib import admin
from django.urls import path
from libros import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.listadoLibros),
    path('libros/', views.listadoLibros),
    path('agregarlibros/', views.agregarLibros),
    path('actualizarLibros/<int:id>', views.actualizarLibros, name='actualizarLibros'),
    path('eliminar/<int:id>/', views.eliminarLibros, name='eliminarLibros'),
    path('libros/', views.listadoLibros, name='libros'),
]
