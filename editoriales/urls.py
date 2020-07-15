from django.conf.urls import url
from django.urls import path

import editoriales
from editoriales.views import editorial

urlpatterns = [
url(r'^listar/$', editorial, name='editorial')
]
