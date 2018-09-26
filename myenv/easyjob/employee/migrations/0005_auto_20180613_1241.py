# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_auto_20180606_1101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='skill',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
