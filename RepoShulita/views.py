from django.shortcuts import render, redirect, reverse
from django.contrib.admin.views.decorators import staff_member_required
from django.core.mail import send_mail
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from .models import Persona, Boleta, Producto
from .forms import FormPersona, FormProducto

import numpy

# Create your views here.


def index(request):
    return render(request, "index.html", {"titulo": "Index"})


def catalogo(request):
    prod=Producto.objects.all()
    return render(request, "catalogo.html", {"titulo": "Catalogo", "prods":prod})


def confirmacion(request):
    return render(request, "confirmacion.html", {"titulo": "Confirmacion"})


def addProducto(request):

    if request.method == "POST":
        form = FormProducto(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            Producto.objects.create(
                nombre=data.get("nombre"),
                categoria=data.get("categoria"),
                precio=data.get("precio"),
                stock=data.get("stock"),
                descripcion=data.get("descripcion"),
                foto=request.FILES["foto"])
        return redirect("catalogo")
    else:
        form = FormProducto()
    return render(request, "addProducto.html", {"titulo": "Añadir producto", "form": form})

def addCarrito(request, idProducto):
    producto=Producto.objects.get(idProducto=idProducto)
    return render(request,"contacto.html", {"prods": prods})


def contacto(request):
    return render(request, "contacto.html", {"titulo": "Contacto"})
