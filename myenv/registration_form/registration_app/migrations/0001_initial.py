# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('Model', models.CharField(max_length=30)),
                ('Year', models.DateField()),
                ('Color', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='License',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('First_Name', models.CharField(max_length=30)),
                ('Last_Name', models.CharField(max_length=30)),
                ('Address', models.CharField(max_length=30)),
                ('Phone_No', models.CharField(max_length=30)),
                ('Dob', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('Register', models.BooleanField()),
                ('Car', models.ForeignKey(to='registration_app.Car')),
                ('License', models.ForeignKey(to='registration_app.License')),
            ],
        ),
    ]
