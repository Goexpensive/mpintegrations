# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20150529_0429'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='mp_email',
            field=models.EmailField(max_length=254, null=True, blank=True),
        ),
    ]
