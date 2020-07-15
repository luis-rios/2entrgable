from django.shortcuts import render

# Create your views here.
from libros.models import Libro


def libros(request):
    libros = Libro.object.all()
    context = {
        'libros': libros
    }
    return render(request, 'libros/listar.html', context=context)