# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('museos', '0014_auto_20180520_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagpersonal',
            name='Titulo',
            field=models.TextField(default='', null=True),
        ),
    ]
