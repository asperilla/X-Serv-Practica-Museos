# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('museos', '0005_remove_museo_fax'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comentario',
            name='Usuario',
        ),
    ]
