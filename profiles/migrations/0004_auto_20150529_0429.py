# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20150529_0414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='access_token',
            field=models.CharField(null=True, max_length=254, blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='mercadopago_user_id',
            field=models.BigIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='public_key',
            field=models.CharField(null=True, max_length=254, blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='refresh_token',
            field=models.CharField(null=True, max_length=254, blank=True),
        ),
    ]
