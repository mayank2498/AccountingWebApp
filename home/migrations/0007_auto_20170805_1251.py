# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-05 07:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_remove_voucher_firm'),
    ]

    operations = [
        migrations.AddField(
            model_name='ledger',
            name='temp1',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='ledger',
            name='temp2',
            field=models.FloatField(default=0.0),
        ),
    ]
