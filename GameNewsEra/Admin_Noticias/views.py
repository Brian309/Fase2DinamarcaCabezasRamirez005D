from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.template import Template, Context
from . models import Autor, Consola, Noticia
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import render
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


def game1(request):

    return render(request,'pgs/game-1.html', context={},)


def game2(request):

    return render(request,'pgs/game-2.html', context={},)


def game3(request):

    return render(request,'pgs/game-3.html', context={},)


def game4(request):

    return render(request,'pgs/game-4.html', context={},)

# CRUD Autor
class AutorCreate(CreateView):

    model = Autor
    fields = '__all__'

class AutorUpdate(UpdateView):

    model = Autor
    fields = ['id_autor','nom_autor','educacion','numero','correo']

class AutorDelete(DeleteView):
    
    model = Autor
    success_url = reverse_lazy('index')

class AutorDetailView(generic.DetailView):

    model = Autor

class AutorListView(generic.ListView):

    model = Autor
    template_name = 'templates/admin_noticias/autor_list.html'
    paginate_by = 3

# CRUD Noticia
class NoticiaCreate(CreateView):

    model = Noticia
    fields = '__all__'

class NoticiaUpdate(UpdateView):

    model = Noticia
    fields = ['id_noticia','titulo','descripcion','tipo_de_noticia','autor']

class NoticiaDelete(DeleteView):

    models = Noticia
    success_url = reverse_lazy('index')

class NoticiaDetailView(generic.DetailView):

    model = Noticia

class NoticiaListView(generic.ListView):

    model = Noticia
    template_name = 'templates/admin_noticias/noticia_list.html'
    paginate_by = 10

#CRUD Consola
class ConsolaCreate(CreateView):
    model = Consola
    fields = '__all__'
    initial = {'generacion':'Novena Generacion'}
    

class ConsolaUpdate(UpdateView):
    model = Consola
    fields = ['id_consola','nombre','generacion']

class ConsolaDelete(DeleteView):
    model = Consola
    success_url = reverse_lazy('index')

class ConsolaDetailView(generic.DetailView):
    model = Consola

class ConsolaListView(generic.ListView):

    model = Consola
    template_name = 'templates/admin_noticias/consola_list.html'
    paginate_by = 3





