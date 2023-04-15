import datetime
from django.shortcuts import render 
from django.http import HttpResponse
from hola_mundo.models import Persona, Tarea, Trabajo
from hola_mundo.forms import PersonaForm, TrabajoForm, TareaForm 
from django.views.generic import ListView
from django.shortcuts import render, redirect
from .forms import TrabajoForm
from .models import Trabajo
from .models import Tarea
from .views import busquedaTarea 



def saludar(request):
    return HttpResponse("Hola mundo !!")
def saludar_a(request, alguien):
    return HttpResponse(f"hola como estas {alguien}")
def sumar(request, a, b):
    return HttpResponse(f"El resultado de {a} + {b} = {a+b} ")


def mostrar_tareas(request):
    tareas = Tarea.objects.all()
    total_tareas = len(tareas)
    context = {
        "tareas": tareas,
        "total_tareas": total_tareas,
        "form": TareaForm(),
    }
    return render(request, "hola_mundo/tareas.html", context)


def crear_tarea(request):

    f = TareaForm(request.POST)
    context = {
        "form": f

    }
    
    if f.is_valid():
        Tarea(nombre= f.data["nombre"]).save()
        context['form'] = TareaForm()

    context["tareas"] = Tarea.objects.all()
    context["total_tareas"] = len(Tarea.objects.all())

    return render(request, "hola_mundo/tareas.html", context)

def busquedaTarea(request):
    return render(request, "hola-mundo/busquedaTarea.html")


def buscar(request):
    if request.GET["camada"]:
    
    
        tarea = request.GET['tarea']
        tareas = Tarea.objects.filter(tarea_icontains=tareas)

    else:
        respuesta = "No existe esta tarea"
    return HttpResponse(respuesta)

def mostrar_personas(request):
    personas = Persona.objects.all()
    total_personas = len(personas)
    context = {
        "personas": personas,
        "total_personas": total_personas,
        "form": PersonaForm(),
    }
    return render(request, "hola_mundo/personas.html", context)


def crear_persona(request):

    f = PersonaForm(request.POST)
    context = {
        "form": f

    }
    
    if f.is_valid():
        Persona(nombre= f.data["nombre"], apellido=f.data["apellido"], fecha_nacimiento=f.data["fecha_nacimiento"]).save()
        context['form'] = PersonaForm()

    context["personas"] = Persona.objects.all()
    context["total_personas"] = len(Persona.objects.all())

    return render(request, "hola_mundo/personas.html", context)


def mostrar_trabajos(request):
    trabajos = Trabajo.objects.all()
    total_trabajos = len(trabajos)
    context = {
        "trabajos": trabajos,
        "total_trabajos": total_trabajos,
        "form": TrabajoForm(),
    }
    return render(request, "hola_mundo/trabajos.html", context)



def crear_trabajo(request):
    if request.method == 'POST':
        form = TrabajoForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Trabajo.objects.create(
                apellido=data['apellido'],
                empresa=data['empresa'],
                puesto=data['puesto'],
                fecha_de_inicio=data.get('fecha_de_inicio') if data.get('fecha_de_inicio') else datetime.now()
            ).save()
            return redirect('trabajos')
    else:
        form = TrabajoForm()

    trabajos = Trabajo.objects.all()
    total_trabajos = len(trabajos)
    context = {
        'form': form,
        'trabajos': trabajos,
        'total_trabajos': total_trabajos
    }
    return render(request, 'hola_mundo/trabajos.html', context)



 

