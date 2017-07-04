# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-07-03 13:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='F0101',
            fields=[
                ('clave', models.IntegerField(db_column='ABAN8', primary_key=True, serialize=False)),
                ('nombre', models.CharField(db_column='ABALPH', max_length=40)),
                ('tipo', models.CharField(db_column='ABAT1', max_length=3)),
                ('rfc', models.CharField(db_column='ABTAX', max_length=20)),
            ],
            options={
                'db_table': '"CRPDTA"."F0101"',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='F5903000',
            fields=[
                ('ftgenkey', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('fttax', models.CharField(blank=True, max_length=20, null=True)),
                ('fttaxs', models.CharField(blank=True, max_length=20, null=True)),
                ('ftbrtpo', models.CharField(max_length=3)),
                ('fttxr1', models.IntegerField(default=0)),
                ('fttxr2', models.IntegerField(default=0)),
                ('fttxr3', models.IntegerField(default=0)),
                ('fttxr4', models.IntegerField(default=0)),
                ('fttxr5', models.IntegerField(default=0)),
                ('ftafa1', models.IntegerField(default=0)),
                ('ftafa2', models.IntegerField(default=0)),
                ('ftafa3', models.IntegerField(default=0)),
                ('ftafa4', models.IntegerField(default=0)),
                ('ftafa5', models.IntegerField(default=0)),
                ('ftcrcd', models.CharField(blank=True, max_length=3, null=True)),
                ('ftcrr', models.IntegerField(default=0)),
                ('ftamrt1', models.IntegerField(default=0)),
                ('ftamrt2', models.IntegerField(default=0)),
                ('ftamrt3', models.IntegerField(default=0)),
                ('ftlo01', models.CharField(blank=True, max_length=5, null=True)),
                ('fturab', models.IntegerField(default=0)),
                ('fturat', models.IntegerField(default=0)),
                ('fturcd', models.CharField(blank=True, max_length=2, null=True)),
                ('fturdt', models.IntegerField(default=0)),
                ('fturrf', models.CharField(blank=True, max_length=15, null=True)),
                ('ftuser', models.CharField(blank=True, max_length=10, null=True)),
                ('ftpid', models.CharField(blank=True, max_length=10, null=True)),
                ('ftjobn', models.CharField(blank=True, max_length=10, null=True)),
                ('ftupmj', models.IntegerField(default=0)),
                ('ftupmt', models.IntegerField(default=0)),
                ('ftivd', models.IntegerField(default=0)),
                ('ftan8', models.IntegerField(default=0)),
            ],
            options={
                'db_table': '"CRPDTA"."F5903000"',
                'managed': False,
            },
        ),
    ]
