# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-09-24 13:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0015_auto_20180924_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='tag',
            field=models.CharField(max_length=100),
        ),
    ]