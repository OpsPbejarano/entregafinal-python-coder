from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy
from bloggeneral.models import *
# Create your views here.

class home(ListView):
    model = BlogModel 
    template_name= "bloggeneral/home.html"

class crearBlog(CreateView):
    model= BlogModel
    template_name= "bloggeneral/crear.html"
    success_url = reverse_lazy("home")
    fields = ["titulo", "subtitulo", "descripcion", "cuerpo", "autor"]

def CrearBlog(request):
    return HttpResponse("Crear")

def ModificarBlog(request):
    return HttpResponse("Modificar")

class EliminarBlog(DeleteView):
    model = BlogModel
    template_name = "bloggeneral/confirm_delete.html"
    success_url = reverse_lazy("home")

