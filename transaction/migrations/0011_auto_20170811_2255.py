# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-11 17:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0010_auto_20170805_1251'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='amount_left',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='expense',
            name='transaction_type',
            field=models.CharField(choices=[('Cash', 'Cash'), ('Bank', 'Bank')], default='Cash', max_length=50),
        ),
        migrations.AlterField(
            model_name='expense',
            name='voucher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.Voucher'),
        ),
        migrations.AlterField(
            model_name='impress',
            name='transaction_type',
            field=models.CharField(choices=[('Cash', 'Cash'), ('Bank', 'Bank')], default='Cash', max_length=50),
        ),
        migrations.AlterField(
            model_name='impress',
            name='voucher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.Voucher'),
        ),
        migrations.AlterField(
            model_name='receive',
            name='transaction_type',
            field=models.CharField(choices=[('Cash', 'Cash'), ('Bank', 'Bank')], default='Cash', max_length=50),
        ),
        migrations.AlterField(
            model_name='receive',
            name='voucher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.Voucher'),
        ),
    ]