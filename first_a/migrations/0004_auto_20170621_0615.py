# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-21 03:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_a', '0003_auto_20170621_0613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pupil',
            name='first_name',
            field=models.CharField(choices=[('Рахмонов Хайём', 'Рахмонов Хайём'), ('РЛфырало Оофыола', 'РЛфырало Оофыола')], max_length=50),
        ),
    ]