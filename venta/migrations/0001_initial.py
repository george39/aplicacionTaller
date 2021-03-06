# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-16 02:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('producto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('codigo_venta', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('fecha_venta', models.DateTimeField(auto_now_add=True)),
                ('cantidad', models.IntegerField()),
                ('valor_venta', models.IntegerField()),
                ('id_producto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='producto.Producto')),
            ],
        ),
    ]
