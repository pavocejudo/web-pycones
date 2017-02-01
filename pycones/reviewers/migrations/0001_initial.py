# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-31 12:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('proposals', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('relevance', models.PositiveIntegerField(blank=True, help_text='Puntuación del 1 al 10', null=True, verbose_name='Relevancia')),
                ('interest', models.PositiveIntegerField(blank=True, help_text='Puntuación del 1 al 10', null=True, verbose_name='Interés General')),
                ('newness', models.PositiveIntegerField(blank=True, help_text='Puntuación del 1 al 10', null=True, verbose_name='Novedad')),
                ('notes', models.TextField(blank=True, null=True, verbose_name='Notas del revisor')),
                ('conflict', models.BooleanField(default=False, verbose_name='¿Existe un conflico de intereses?')),
                ('finished', models.BooleanField(default=False, verbose_name='¿Revisión finalizada?')),
                ('proposal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='proposals.Proposal')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reviewer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='reviewer', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
        migrations.AlterUniqueTogether(
            name='review',
            unique_together=set([('user', 'proposal')]),
        ),
    ]