from django.shortcuts import render, redirect, reverse
from django.contrib.admin.views.decorators import staff_member_required
from django.core.mail import send_mail
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from .models import Persona,Boleta,Producto

import numpy

# Create your views here.

def index(request):
	return render(request, "index.html", { "titulo": "Index" })

def catalogo(request):
	return render(request, "catalogo.html", { "titulo": "Catalogo" })

def confirmacion(request):
	return render(request, "confirmacion.html", { "titulo": "Confirmacion" })

def contacto(request):
	return render(request, "contacto.html", { "titulo": "Contacto" })
