from django.contrib import admin
from hola_mundo.models import Tarea
from hola_mundo.models import Persona
from hola_mundo.models import Trabajo

admin.site.register(Tarea)
admin.site.register(Persona)
admin.site.register(Trabajo)

# Register your models here.
