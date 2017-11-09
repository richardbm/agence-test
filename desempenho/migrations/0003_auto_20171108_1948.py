# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-08 19:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desempenho', '0002_auto_20171108_1937'),
    ]

    operations = [
        migrations.CreateModel(
            name='PermissaoSistema',
            fields=[
                ('co_usuario', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('co_tipo_usuario', models.BigIntegerField(default=0)),
                ('co_sistema', models.BigIntegerField(default=0)),
                ('dt_atualizacao', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='caousuario',
            name='nu_matricula',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterUniqueTogether(
            name='permissaosistema',
            unique_together=set([('co_usuario', 'co_tipo_usuario', 'co_sistema', 'dt_atualizacao')]),
        ),
    ]
