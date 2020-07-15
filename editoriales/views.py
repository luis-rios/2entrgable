from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from editoriales.models import Editorial


def editorial(request):
    editorial = Editorial.objects.all()
    context = {
        'editorial': editorial
    }
    return render(request, 'editorial/listar.html', context=context)