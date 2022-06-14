from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("home") 

def CrearBlog(request):
    return HttpResponse("Crear")

def ModificarBlog(request):
    return HttpResponse("Modificar")

def EliminarBlog(request):
    return HttpResponse("Eliminar")

