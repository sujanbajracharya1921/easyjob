# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_auto_20180507_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
