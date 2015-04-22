# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preferences', '0003_auto_20150422_0203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preferences',
            name='unit_price',
            field=models.FloatField(),
        ),
    ]
