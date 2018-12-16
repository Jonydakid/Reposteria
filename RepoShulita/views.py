from django.shortcuts import render, redirect, reverse
from django.contrib.admin.views.decorators import staff_member_required
from django.core.mail import send_mail
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from .models import Persona,Boleta,Producto

import numpy

# Create your views here.

def index(request):
	return render(request, "nosotros.html", { "titulo": "Nosotros" })

def catalogo(request):
	return render(request, "nosotros.html", { "titulo": "Nosotros" })

def confirmacion(request):
	return render(request, "nosotros.html", { "titulo": "Nosotros" })

def contacto(request):
	return render(request, "nosotros.html", { "titulo": "Nosotros" })
