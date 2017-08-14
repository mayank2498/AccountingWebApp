# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-12 08:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0013_auto_20170812_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='voucher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.Voucher'),
        ),
        migrations.AlterField(
            model_name='impress',
            name='voucher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.Voucher'),
        ),
        migrations.AlterField(
            model_name='receive',
            name='voucher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.Voucher'),
        ),
    ]