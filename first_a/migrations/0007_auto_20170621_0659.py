# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-21 03:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_a', '0006_auto_20170621_0652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pupil',
            name='pupil',
            field=models.CharField(choices=[('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('нб', 'нб')], max_length=50, verbose_name='Сидоров Валентин'),
        ),
    ]