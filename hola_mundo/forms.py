from django import forms

class PersonaForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    fecha_nacimiento = forms.DateField()

class BuscarPersonasForms(forms.Form):
    criterio_nombre = forms.CharField(max_length=100)

class TrabajoForm(forms.Form):
    apellido = forms.CharField(max_length=100)
    empresa = forms.CharField(max_length=50)
    puesto = forms.CharField(max_length=100)
    fecha_de_inicio = forms.DateTimeField()

class TareaForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    


    