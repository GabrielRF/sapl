# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-10 13:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0023_auto_20161009_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autor',
            name='nome',
            field=models.CharField(blank=True, max_length=50, verbose_name='Nome do Autor'),
        ),
        migrations.AlterField(
            model_name='autor',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.TipoAutor', verbose_name='Tipo do Autor'),
        ),
    ]