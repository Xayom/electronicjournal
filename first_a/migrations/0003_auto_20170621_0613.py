# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-21 03:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_a', '0002_auto_20170621_0611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pupil',
            name='first_name',
            field=models.CharField(choices=[(1, 'Рахмонов Хайём'), (2, 'РЛфырало Оофыола')], max_length=50),
        ),
    ]