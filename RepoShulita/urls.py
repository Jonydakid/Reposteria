from django.conf.urls import url
from django.urls import path
from . import views
""" Urls pagina"""
urlpatterns = [
	url(r"^confirmacion/$", views.confirmacion, name = "confirmacion"),
	url(r"^catalogo/$", views.catalogo, name = "catalogo"),
	url(r"^contacto/$", views.contacto, name = "contacto"),
	url(r"^$", views.index, name = "indice"),
]
