# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-04 08:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviewers', '0003_auto_20170622_2129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='score',
            field=models.FloatField(blank=True, help_text='Puntuación del 1.0 al 4.0', null=True, verbose_name='Puntuación'),
        ),
    ]
