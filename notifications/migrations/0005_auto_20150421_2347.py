# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0004_auto_20150421_2305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notifications',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='notifications',
            name='last_modified_date',
            field=models.DateTimeField(null=True, auto_now=True),
        ),
    ]
