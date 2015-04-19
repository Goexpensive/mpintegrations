# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0002_auto_20150419_1724'),
    ]

    operations = [
        migrations.AddField(
            model_name='notifications',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 4, 19, 17, 57, 9, 572748, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='notifications',
            name='last_modified_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 19, 17, 57, 27, 492133, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
