# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('preferences', '0009_auto_20150430_0244'),
    ]

    operations = [
        migrations.AddField(
            model_name='preferencetemplates',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 30, 3, 43, 16, 97890, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
