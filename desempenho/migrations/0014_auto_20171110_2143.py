# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-10 21:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('desempenho', '0013_auto_20171110_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caofatura',
            name='co_os',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='faturas', to='desempenho.CaoOs'),
        ),
    ]
