from django.conf.urls import url

from libros.views import libros

urlpatterns = [
    url(r'^listar/$', libros, name='libro')
]