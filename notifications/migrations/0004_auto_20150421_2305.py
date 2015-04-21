# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0003_auto_20150419_1757'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notifications',
            name='mp_id',
        ),
        migrations.AlterField(
            model_name='notifications',
            name='id',
            field=models.BigIntegerField(serialize=False, primary_key=True),
        ),
    ]
