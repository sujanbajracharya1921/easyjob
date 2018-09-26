# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_cv_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cv',
            name='employee',
            field=models.OneToOneField(to='employee.EmployeeProfile'),
        ),
        migrations.AlterField(
            model_name='degree',
            name='employee',
            field=models.OneToOneField(to='employee.EmployeeProfile'),
        ),
        migrations.AlterField(
            model_name='employeeprofile',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='experience',
            name='employee',
            field=models.OneToOneField(to='employee.EmployeeProfile'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='employee',
            field=models.OneToOneField(to='employee.EmployeeProfile'),
        ),
        migrations.AlterField(
            model_name='training',
            name='employee',
            field=models.OneToOneField(to='employee.EmployeeProfile'),
        ),
    ]
