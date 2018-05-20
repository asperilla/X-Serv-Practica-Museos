# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('museos', '0007_personal'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pagina',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('FechaSeleccion', models.DateField(auto_now_add=True)),
                ('MuseoSeleccionado', models.ForeignKey(to='museos.Museo')),
                ('Usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='personal',
            name='MuseoSeleccionado',
        ),
        migrations.RemoveField(
            model_name='personal',
            name='Usuario',
        ),
        migrations.DeleteModel(
            name='Personal',
        ),
    ]
