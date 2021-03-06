# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-03 13:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0005_auto_20170803_1108'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(default=0.0)),
                ('transaction_type', models.CharField(choices=[(b'Cash', b'Cash'), (b'Bank', b'Bank')], default=b'Cash', max_length=50)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('ledger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Ledger')),
                ('voucher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Voucher')),
            ],
        ),
        migrations.CreateModel(
            name='Impress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(default=0.0)),
                ('transaction_type', models.CharField(choices=[(b'Cash', b'Cash'), (b'Bank', b'Bank')], default=b'Cash', max_length=50)),
                ('pending', models.BooleanField(default=True)),
                ('amount_left', models.FloatField(default=0.0)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('ledger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Ledger')),
                ('voucher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Voucher')),
            ],
        ),
        migrations.CreateModel(
            name='Receive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(default=0.0)),
                ('transaction_type', models.CharField(choices=[(b'Cash', b'Cash'), (b'Bank', b'Bank')], default=b'Cash', max_length=50)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('ledger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Ledger')),
                ('voucher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Voucher')),
            ],
        ),
    ]
