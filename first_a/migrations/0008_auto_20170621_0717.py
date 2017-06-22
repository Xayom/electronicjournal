# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-21 04:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('first_a', '0007_auto_20170621_0659'),
    ]

    operations = [
        migrations.AddField(
            model_name='pupil',
            name='data_add',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата'),
        ),
        migrations.AddField(
            model_name='pupil',
            name='rating',
            field=models.CharField(choices=[('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('нб', 'нб')], default=2, max_length=50, verbose_name='Оценка'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pupil',
            name='pupil',
            field=models.CharField(choices=[('Рахмонов Хайём', 'Рахмонов Хайём'), ('Абдулоев Мухаммад', 'Абдулоев Мухаммад'), ('Сирочов Ахмад', 'Сирочов Ахмад'), ('Сидоров Валентин', 'Сидоров Валентин')], max_length=50, verbose_name='Ученик'),
        ),
    ]
