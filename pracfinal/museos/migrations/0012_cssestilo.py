# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('museos', '0011_auto_20180520_1119'),
    ]

    operations = [
        migrations.CreateModel(
            name='CssEstilo',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('Titulo', models.TextField(default='')),
                ('Color', models.TextField(default='white', max_length='30')),
                ('TamañoLetra', models.TextField(default='h3')),
                ('Usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
