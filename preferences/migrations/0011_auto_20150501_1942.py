# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preferences', '0010_preferencetemplates_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='preferencetemplates',
            name='slug',
            field=models.SlugField(unique=True, default=123),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='preferencetemplates',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
