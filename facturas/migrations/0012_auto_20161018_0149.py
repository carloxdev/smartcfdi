# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-18 01:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturas', '0011_auto_20161017_2317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resumen',
            name='tipo',
            field=models.CharField(choices=[('PROVEEDORES', 'FACTURAS DE PROVEEDORES'), ('CLIENTES', 'FACTURAS DE CLIENTES'), ('EMPLEADOS', 'COMPROBANTES DE EMPLEADOS')], max_length=12),
        ),
    ]
