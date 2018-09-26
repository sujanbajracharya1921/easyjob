# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Degree',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('degree_name', models.CharField(max_length=30)),
                ('institution', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=30)),
                ('portfolio', models.URLField()),
                ('contact', models.CharField(max_length=10)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('company', models.CharField(max_length=30)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True)),
                ('employee', models.ForeignKey(to='company.EmployeeProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('skill', models.CharField(max_length=30)),
                ('employee', models.ForeignKey(to='company.EmployeeProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('training_name', models.CharField(max_length=30)),
                ('institute', models.CharField(max_length=30)),
                ('employee', models.ForeignKey(to='company.EmployeeProfile')),
            ],
        ),
        migrations.AddField(
            model_name='degree',
            name='employee',
            field=models.ForeignKey(to='company.EmployeeProfile'),
        ),
    ]
