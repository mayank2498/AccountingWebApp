# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-08 14:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20170820_1204'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ledger',
            name='balance_minus',
        ),
        migrations.RemoveField(
            model_name='ledger',
            name='balance_plus',
        ),
        migrations.AlterField(
            model_name='ledger',
            name='type',
            field=models.CharField(choices=[('Supplier', 'Supplier'), ('Customer', 'Customer'), ('Employee', 'Employee'), ('Personal', 'Personal'), ('Others', 'Others')], default='Others', max_length=50),
        ),
    ]