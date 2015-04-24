# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preferences', '0005_auto_20150424_0248'),
    ]

    operations = [
        migrations.AddField(
            model_name='preferences',
            name='expiration_date_from',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='preferences',
            name='expiration_date_to',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='preferences',
            name='expires',
            field=models.NullBooleanField(),
        ),
    ]
