"""mi_primer_mvt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from hola_mundo import views
from hola_mundo.views import busquedaTarea, buscar, saludar, saludar_a, sumar, mostrar_tareas, crear_tarea, mostrar_personas, crear_persona, crear_trabajo, mostrar_trabajos  
from SocialTravel.views import index
urlpatterns = [    
    path('admin/', admin.site.urls),
    path('hola.mundo/saludar', saludar), 
    path('hola.mundo/saludar-a/<alguien>', saludar_a),
    path('hola.mundo/sumar/<int:a>/<int:b>', sumar),
    path('mis-tareas/<criterio>', mostrar_tareas, name="mis-tareas"),
    path('', index),
    path('hola.mundo/personas', mostrar_personas, name="personas"),
    path('personas', mostrar_personas, name="personas"),
    path('personas/create', crear_persona, name="personas-create"),
    path('tareas', mostrar_tareas, name = "tareas"),
    path('tareas/create', crear_tarea, name="tareas-create"),
    path('trabajos', crear_trabajo, name="trabajos"),
    path('busquedaTarea', views.busquedaTarea, name="BusquedaTarea"),
    path('buscar/', views.buscar)

    
    



]
    
    
