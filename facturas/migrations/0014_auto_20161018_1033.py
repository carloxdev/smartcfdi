# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-18 10:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturas', '0013_auto_20161018_1030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resumen',
            name='total',
            field=models.DecimalField(decimal_places=4, default=0.0, max_digits=20),
        ),
    ]
