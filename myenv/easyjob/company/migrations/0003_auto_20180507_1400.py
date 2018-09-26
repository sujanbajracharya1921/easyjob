# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('company', '0002_cv'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
            ],
        ),
        migrations.CreateModel(
            name='CompanyProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('company_name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=30)),
                ('contact_no', models.CharField(max_length=10)),
                ('portfolio', models.URLField(blank=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=30)),
                ('tag', models.CharField(max_length=30)),
                ('company', models.ForeignKey(to='company.CompanyProfile')),
            ],
        ),
        migrations.RemoveField(
            model_name='cv',
            name='employee',
        ),
        migrations.RemoveField(
            model_name='degree',
            name='employee',
        ),
        migrations.RemoveField(
            model_name='employeeprofile',
            name='user',
        ),
        migrations.RemoveField(
            model_name='experience',
            name='employee',
        ),
        migrations.RemoveField(
            model_name='skill',
            name='employee',
        ),
        migrations.RemoveField(
            model_name='training',
            name='employee',
        ),
        migrations.DeleteModel(
            name='Cv',
        ),
        migrations.DeleteModel(
            name='Degree',
        ),
        migrations.DeleteModel(
            name='EmployeeProfile',
        ),
        migrations.DeleteModel(
            name='Experience',
        ),
        migrations.DeleteModel(
            name='Skill',
        ),
        migrations.DeleteModel(
            name='Training',
        ),
        migrations.AddField(
            model_name='application',
            name='cv',
            field=models.ForeignKey(to='employee.Cv'),
        ),
        migrations.AddField(
            model_name='application',
            name='vacancy',
            field=models.ForeignKey(to='company.Vacancy'),
        ),
    ]
