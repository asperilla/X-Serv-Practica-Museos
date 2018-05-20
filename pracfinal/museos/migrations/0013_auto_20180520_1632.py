# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('museos', '0012_cssestilo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cssestilo',
            name='Usuario',
        ),
        migrations.AddField(
            model_name='pagpersonal',
            name='Color',
            field=models.TextField(default='white', max_length='30'),
        ),
        migrations.AddField(
            model_name='pagpersonal',
            name='TamañoLetra',
            field=models.TextField(default='h3'),
        ),
        migrations.AddField(
            model_name='pagpersonal',
            name='Titulo',
            field=models.TextField(default=''),
        ),
        migrations.DeleteModel(
            name='CssEstilo',
        ),
    ]
