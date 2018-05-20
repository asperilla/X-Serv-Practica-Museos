# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('museos', '0010_pagpersonal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='museo',
            name='Accesibilidad',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='museo',
            name='CodigoPostal',
            field=models.TextField(default=''),
        ),
    ]
