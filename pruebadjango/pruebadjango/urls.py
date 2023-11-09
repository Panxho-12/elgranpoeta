from django.contrib import admin
from django.urls import path
from libros import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('libros/', views.listadoLibros),
    path('agregarlibros/', views.agregarLibros)

]