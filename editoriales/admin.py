from django.contrib import admin

# Register your models here.
from editoriales.models import Editorial
from libros.models import Libro

admin.site.register(Editorial)