from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.index, name='index'),
    path('videogames/', views.videogames, name='videogames'),
    path('consolas/', views.consolas, name='consolas'),
    path('contacto/', views.contacto, name='contacto'),
    path('gracias/', views.gracias, name='gracias'),
]