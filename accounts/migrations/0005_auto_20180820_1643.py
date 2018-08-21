# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-20 16:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20180820_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facultyprofile',
            name='group',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to='auth.Group'),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='group',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to='auth.Group'),
        ),
    ]
