# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('museos', '0009_auto_20180520_0731'),
    ]

    operations = [
        migrations.CreateModel(
            name='PagPersonal',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('FechaSeleccion', models.DateField(auto_now_add=True)),
                ('MuseoSeleccionado', models.ForeignKey(to='museos.Museo')),
                ('Usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
