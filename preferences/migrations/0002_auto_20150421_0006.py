# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('preferences', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='preferences',
            old_name='quantity',
            new_name='items_quantity',
        ),
        migrations.RenameField(
            model_name='preferences',
            old_name='unit_price',
            new_name='items_unit_price',
        ),
        migrations.RemoveField(
            model_name='preferences',
            name='title',
        ),
        migrations.AddField(
            model_name='preferences',
            name='items_title',
            field=models.CharField(default=datetime.datetime(2015, 4, 21, 0, 6, 6, 355197, tzinfo=utc), max_length=255),
            preserve_default=False,
        ),
    ]
