# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2019-01-10 15:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('protocoloadm', '0014_auto_20190110_1300'),
    ]

    operations = [
        migrations.AddField(
            model_name='protocolo',
            name='timestamp_data_hora_manual',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]