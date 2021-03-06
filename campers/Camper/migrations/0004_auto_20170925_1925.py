# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-25 19:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Camper', '0003_auto_20170925_1911'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='camper',
            name='category_id',
        ),
        migrations.AlterField(
            model_name='camper',
            name='age',
            field=models.BigIntegerField(choices=[(13, '13'), (14, '14'), (15, '15'), (16, '16'), (17, '17'), (18, '18')]),
        ),
        migrations.AlterField(
            model_name='camper',
            name='category',
            field=models.CharField(choices=[('singer', 'Singer'), ('guitarist', 'Guitarist'), ('drummer', 'Drummer'), ('bassist', 'Bassist'), ('keyboardist', 'Keyboardist'), ('instrumentalist', 'Instrumentalist')], max_length=100),
        ),
        migrations.AlterField(
            model_name='camper',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=10),
        ),
        migrations.AlterField(
            model_name='camper',
            name='rank',
            field=models.BigIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4')]),
        ),
    ]
