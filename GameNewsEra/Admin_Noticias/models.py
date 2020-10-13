from django.db import models
from django.urls import reverse
import uuid

# Create your models here.

class Autor(models.Model):

    id_autor = models.UUIDField(primary_key = True, default = uuid.uuid4, help_text = 'Indique el ID del Autor de Noticia')
    nom_autor = models.TextField(max_length = 50)

    NIVEL_EDUCACIONAL = (
        ('UV', 'Universidad'),
        ('TC', 'Tecnico Profesional'),
        ('SC', 'Secundaria Completa'),
        ('NA', 'Ninguno'),
    )

    educacion =  models.CharField(max_length = 2, choices = NIVEL_EDUCACIONAL, default = 'NA')
    numero = models.IntegerField(max_length = 9, blank = True, null = True)
    correo = models.EmailField(max_length = 50, error_messages = {"Error": "Digite un formato válido!"})

    def __str__(self):

        return f'{self.id_autor}, {self.nom_autor}'


class Tipo_Noticia(models.Model):

    id_tipo = models.UUIDField(primary_key = True, default = uuid.uuid4)
    nom_tipo = models.CharField(max_length = 50)
    descripcion = models.TextField(max_length = 100)

    def __str__(self):

        return self.id_tipo

class Noticia(models.Model):

    id_noticia = models.UUIDField(primary_key = True, default = uuid.uuid4, help_text = 'Indique el ID de la Noticia')
    titulo = models.CharField(max_length = 50)
    descripcion = models.TextField(max_length = 100)
    tipo_noticia = models.ManyToManyField(Tipo_Noticia)
    autor = models.ForeignKey(Autor, on_delete = models.SET_NULL, null= True)

    def __str__(self):

        return f'{self.id_noticia}, {self.titulo}' 

class Consola(models.Model):

    id_consola = models.UUIDField(primary_key = True, default = uuid.uuid4, help_text = 'Indique el ID de la Noticia')
    nombre = models.CharField(max_length = 50)
    generacion = models.CharField(max_length = 25)

    def __str__(self):

        return self.id_consola

