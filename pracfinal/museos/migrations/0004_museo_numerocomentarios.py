# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('museos', '0003_comentario'),
    ]

    operations = [
        migrations.AddField(
            model_name='museo',
            name='NumeroComentarios',
            field=models.IntegerField(default='0'),
        ),
    ]
