# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-21 14:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('joane', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='numeroDoc',
        ),
        migrations.AddField(
            model_name='documento',
            name='cliente',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='joane.Cliente'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='email',
            name='cliente',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='joane.Cliente'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='endereco',
            name='cliente',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='joane.Cliente'),
            preserve_default=False,
        ),
    ]
