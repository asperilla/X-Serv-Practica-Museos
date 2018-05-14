# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Museo',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('Nombre', models.TextField(default='')),
                ('Descripcion', models.TextField(default='')),
                ('Accesibilidad', models.IntegerField(default='0')),
                ('Barrio', models.TextField(default='')),
                ('Distrito', models.TextField(default='')),
                ('Telefono', models.IntegerField(default='0')),
                ('Fax', models.IntegerField(default='0')),
                ('Email', models.TextField(default='')),
                ('Direccion', models.TextField(default='')),
                ('CodigoPostal', models.IntegerField(default='0')),
                ('Enlace', models.TextField(default='')),
            ],
        ),
    ]
