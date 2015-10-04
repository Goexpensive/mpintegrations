# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preferences', '0011_auto_20150501_1942'),
    ]

    operations = [
        migrations.AddField(
            model_name='preferences',
            name='default_shipping_method',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='preferences',
            name='zip_code',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
