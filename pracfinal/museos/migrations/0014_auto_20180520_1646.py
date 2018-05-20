# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('museos', '0013_auto_20180520_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagpersonal',
            name='TamañoLetra',
            field=models.TextField(default='p'),
        ),
    ]
