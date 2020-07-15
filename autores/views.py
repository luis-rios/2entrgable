from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from autores.models import Author


def authors(request):
    autores = Author.objects.all()
    context = {
        'autores': autores
    }
    return render(request, 'autores/listar.html', context=context)
