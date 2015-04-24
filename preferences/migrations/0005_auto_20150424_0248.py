# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preferences', '0004_auto_20150422_0244'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='preferences',
            name='expiration_date_from',
        ),
        migrations.RemoveField(
            model_name='preferences',
            name='expiration_date_to',
        ),
        migrations.RemoveField(
            model_name='preferences',
            name='expires',
        ),
        migrations.AddField(
            model_name='preferences',
            name='additional_info',
            field=models.CharField(null=True, blank=True, max_length=600),
        ),
        migrations.AddField(
            model_name='preferences',
            name='differential_pricing',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='preferences',
            name='identification_number',
            field=models.CharField(null=True, blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name='preferences',
            name='identification_type',
            field=models.CharField(null=True, blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name='preferences',
            name='marketplace',
            field=models.CharField(null=True, blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='preferences',
            name='marketplace_fee',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='preferences',
            name='auto_return',
            field=models.CharField(null=True, blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='preferences',
            name='currency_id',
            field=models.CharField(default='ARS', max_length=3),
            preserve_default=False,
        ),
    ]
