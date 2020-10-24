from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.index, name='index'),
    path('videogames/', views.videogames, name='videogames'),
    path('consolas/', views.consolas, name='consolas'),
    path('contacto/', views.contacto, name='contacto'),
    path('gracias/', views.gracias, name='gracias'),
    path('videogames/game-1', views.game1, name='game-1'),
    path('videogames/game-2', views.game2, name='game-2'),
    path('videogames/game-3', views.game3, name='game-3'),
    path('videogames/game-4', views.game4, name='game-4'),
]

#Noticias de video juegos, index ubicado en una subcarpeta llamada pgs 
