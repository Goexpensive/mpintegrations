# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0005_auto_20150421_2347'),
    ]

    operations = [
        migrations.AddField(
            model_name='notifications',
            name='mp_id',
            field=models.BigIntegerField(default=123),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='notifications',
            name='notification_json',
            field=models.TextField(blank=True, max_length=600, null=True),
        ),
        migrations.AlterField(
            model_name='notifications',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True),
        ),
    ]
