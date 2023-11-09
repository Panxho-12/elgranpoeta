from django.shortcuts import render
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