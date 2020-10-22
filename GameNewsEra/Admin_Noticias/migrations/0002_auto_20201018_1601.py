# Generated by Django 3.1.2 on 2020-10-18 19:01

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Admin_Noticias', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='id_noticia',
            field=models.UUIDField(default=uuid.uuid4, help_text='Indique el ID de la Noticia', primary_key=True, serialize=False),
        ),
    ]
