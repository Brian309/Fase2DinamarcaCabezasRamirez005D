from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
from . models import Autor, Consola, Noticia
from django.views import generic

# Create your views here.

def index(request):

    return render(request, 'index.html', context={},)

def videogames(request):

    return render(request, 'videogames.html', context={},)

def consolas(request):

    return render(request, 'consolas.html', context={},)

def contacto(request):

    nro_autores = Autor.objects.all().count()
    nro_noticias = Noticia.objects.all().count()
    nro_consolas = Consola.objects.all().count()

    return render(request, 'contacto.html', context={'nro_autores':nro_autores, 'nro_noticias':nro_noticias, 'nro_consolas':nro_consolas},)

def gracias(request):

    return render(request, 'gracias.html', context={},)
