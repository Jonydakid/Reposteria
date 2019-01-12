from django.conf.urls import url
from django.urls import path
from . import views
""" Urls pagina"""
urlpatterns = [
	url(r"^confirmacion/$", views.confirmacion, name = "confirmacion"),
	url(r"^catalogo/$", views.catalogo, name = "catalogo"),
	url(r"^contacto/$", views.contacto, name = "contacto"),
	url(r"^addProducto/$", views.addProducto, name = "addProducto"),
	url(r"^catalogo/(?P<idProd>[0-9_]+)$", views.addCarrito, name="addCarrito"),

	url(r"^$", views.index, name = "indice"),
]
