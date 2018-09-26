# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_auto_20180605_1237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cv',
            name='employee',
            field=models.ForeignKey(to='employee.EmployeeProfile'),
        ),
        migrations.AlterField(
            model_name='degree',
            name='employee',
            field=models.ForeignKey(to='employee.EmployeeProfile'),
        ),
        migrations.AlterField(
            model_name='experience',
            name='employee',
            field=models.ForeignKey(to='employee.EmployeeProfile'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='employee',
            field=models.ForeignKey(to='employee.EmployeeProfile'),
        ),
        migrations.AlterField(
            model_name='training',
            name='employee',
            field=models.ForeignKey(to='employee.EmployeeProfile'),
        ),
    ]
