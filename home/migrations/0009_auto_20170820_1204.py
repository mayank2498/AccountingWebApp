# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-20 06:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20170812_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ledger',
            name='type',
            field=models.CharField(choices=[('Supplier', 'Supplier'), ('Customer', 'Customer'), ('Employee', 'Employee'), ('Personal Expense', 'Personal Expense'), ('Others', 'Others')], default='Others', max_length=50),
        ),
    ]
