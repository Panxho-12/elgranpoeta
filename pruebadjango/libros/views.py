from django.shortcuts import render, redirect
from django.http import HttpResponse
from libros.models import Libros
from libros.forms import FormLibros


# Create your views here.

def index(request):
    return render(request, 'libros/index.html')

def listadoLibros(request):
    libros = Libros.objects.all()
    data = {'libros' : libros}
    return render(request,'libros/libros.html', data)


def agregarLibros(request):
    form = FormLibros()
    if request.method == 'POST' :
        form = FormLibros(request.POST)
        if form.is_valid() :
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request,'libros/agregarlibros.html', data)

def actualizarLibros(request, id):
    libros = Libros.objects.get(id = id)
    form = FormLibros(instance=libros)
    if request.method == 'POST' :
        form = FormLibros(request.POST, instance=libros)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'libros/actualizarlibros.html', data)

def eliminarLibros(request, id):
    try:
        libros = Libros.objects.get(id=id)
        libros.delete()
        return redirect('libros')  
    except Libros.DoesNotExist:
        pass

