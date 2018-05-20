# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('museos', '0008_auto_20180520_0730'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pagina',
            name='MuseoSeleccionado',
        ),
        migrations.RemoveField(
            model_name='pagina',
            name='Usuario',
        ),
        migrations.DeleteModel(
            name='Pagina',
        ),
    ]
