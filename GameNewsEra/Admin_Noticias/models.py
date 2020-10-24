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
    numero = models.IntegerField(blank = True, null = True)
    correo = models.EmailField(max_length = 50, error_messages = {"Error": "Digite un formato válido!"})

    def __str__(self):

        return f'{self.id_autor}, {self.nom_autor}'

class Noticia(models.Model):

    id_noticia = models.UUIDField(primary_key = True, default = uuid.uuid4, help_text = 'Indique el ID de la Noticia')
    titulo = models.CharField(max_length = 50)
    descripcion = models.TextField(max_length = 100)
    tipo_de_noticia = models.CharField(max_length = 50, help_text="Debe indicar el tipo de noticia, por ejemplo novedad, popular etc.")
    autor = models.ForeignKey(Autor, on_delete = models.SET_NULL, null= True)

    def __str__(self):

        return f'{self.id_noticia}, {self.titulo}' 

class Consola(models.Model):

    id_consola = models.UUIDField(primary_key = True, default = uuid.uuid4, help_text = 'Indique el ID de la Noticia')
    nombre = models.CharField(max_length = 50)
    generacion = models.CharField(max_length = 25)

    def __str__(self):

        return str(self.id_consola)

class Formulario(models.Model):

    AREAS_POSTULACION = (
        ('NV', 'Noticias Videojuegos'),
        ('NC', 'Noticias Consolas'),
        ('PG', 'Publicidad Gaming')
    )

    NIVEL_EDUCACIONAL = (
        ('UV', 'Universidad'),
        ('TC', 'Tecnico Profesional'),
        ('SC', 'Secundaria Completa'),
        ('NA', 'Ninguno'),
    )

    id_postulacion = models.UUIDField(primary_key = True, default = uuid.uuid4)
    area_postular = models.CharField(max_length = 2, choices = AREAS_POSTULACION, default = 'NV')
    nombre = models.TextField(max_length = 50)
    apellido = models.TextField(max_length = 50)
    correo = models.EmailField(max_length = 50, error_messages = {"Error": "Digite un formato válido!"})
    numero = models.IntegerField(blank = True, null = True)
    nivel_estudios = models.CharField(max_length = 2, choices = NIVEL_EDUCACIONAL, default = 'NA')
    motivo = models.TextField(max_length = 500)

    def __str__(self):

        return str(self)
