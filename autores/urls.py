from django.conf.urls import url
from django.urls import path

from autores.views import authors


urlpatterns = [
    url(r'^listar/$', authors, name='authors')
]