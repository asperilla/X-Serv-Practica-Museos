# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('museos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='museo',
            name='Fax',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='museo',
            name='Telefono',
            field=models.TextField(default=''),
        ),
    ]
