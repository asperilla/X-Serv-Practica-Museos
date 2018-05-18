# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('museos', '0004_museo_numerocomentarios'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='museo',
            name='Fax',
        ),
    ]
