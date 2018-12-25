from django import forms

BOLET_STATUS = (
    ("Procesado", "Procesado"),
    ("Pagado", "Pagado"),
    ("Recibido", "Recibido")
)


class FormPersona(forms.Form):
    run = forms.CharField(label="RUN", max_length=10, widget=forms.TextInput(
        attrs={"id": "run", "class": "campo", "placeholder": "12345678-9"}))
    nombre = forms.CharField(label="Nombre completo", max_length=120, widget=forms.TextInput(
        attrs={"id": "nombres", "class": "campo", "placeholder": "Ingrese nombres"}))
    fechaNac = forms.DateField(label="Fecha de nacimiento", widget=forms.DateInput(
        attrs={"id": "fechaNac", "class": "campo", "placeholder": "dd/mm/yyyy"}))
    direccion = forms.CharField(label="Dirección", max_length=50, widget=forms.TextInput(
    	attrs={"id": "direccion", "class": "campo", "placeholder": "Ingrese direccion"}))
    correo = forms.EmailField(label="Correo electrónico", max_length=30, widget=forms.EmailInput(
    	attrs={"id": "correo", "class": "campo", "placeholder": "direccioncorreo@correo.com"}))
    telefono = forms.IntegerField(label="Teléfono", required=False, widget=forms.TextInput(
    	attrs={"id": "telefono", "class": "campo", "placeholder": "Ingrese número de teléfono"}))


class FormProducto(forms.Form):
    CATEGORIAS = (
        ("PP", "Panes de Pascua"),
        ("EMP", "Empanadas"),
        ("PA", "Panes Amasados")
    )
    nombre = forms.CharField(label="Nombre", max_length=100, widget=forms.TextInput(
        attrs={"id": "nombre", "class": "campo"}))
    categoria = forms.ChoiceField(label="Categoria", widget=forms.Select(
        attrs={"id": "categoria", "class": "campo", "placeholder": "Categoria"}), choices=CATEGORIAS)
    precio = forms.IntegerField(label="Precio", min_value=0, widget=forms.NumberInput(
        attrs={"id": "precio", "class": "campo", "placeholder": "5000"}))
    stock = forms.IntegerField(label="Stock", min_value=0, widget=forms.NumberInput(
        attrs={"id": "stock", "class": "campo", "placeholder": "1"}))
    foto = forms.ImageField(
        label="Foto",required=False, widget=forms.ClearableFileInput(attrs={"id": "foto", "enctype":"multipart/form-data"}))
    descripcion = forms.CharField(label="Descripcion", max_length=255, widget=forms.TextInput(
        attrs={"id": "descripcion", "class": "campo"}))
