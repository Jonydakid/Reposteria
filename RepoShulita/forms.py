from django import forms

BOLET_STATUS = (
	("Procesado", "Procesado"),
	("Pagado", "Pagado"),
    ("Recibido", "Recibido")
)

class FormPersona(forms.Form):
	run = forms.CharField(label = "RUN", max_length = 10, widget = forms.TextInput(attrs = { "id": "run", "class": "campo", "placeholder": "12345678-9" }))
	nombre = forms.CharField(label = "Nombre completo", max_length = 120, widget = forms.TextInput(attrs = { "id": "nombres", "class": "campo", "placeholder": "Ingrese nombres" }))
	fechaNac = forms.DateField(label = "Fecha de nacimiento", max_length = 20, widget = forms.DateInput(attrs = { "id": "fechaNac", "class": "campo", "placeholder" : "dd/mm/yyyy" }))
    direccion = forms.CharField(label = "Dirección", max_length = 50, widget = forms.TextInput(attrs = { "id": "direccion", "class": "campo", "placeholder" : "Ingrese direccion" }))
	correo = forms.EmailField(label = "Correo electrónico", max_length = 30, widget = forms.EmailInput(attrs = { "id": "correo", "class": "campo", "placeholder": "direccioncorreo@correo.com" }))
	telefono = forms.IntegerField(label = "Teléfono", required = False, widget = forms.TextInput(attrs = { "id": "telefono", "class": "campo", "placeholder": "Ingrese número de teléfono" }))
