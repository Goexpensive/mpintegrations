# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preferences', '0008_auto_20150430_0149'),
    ]

    operations = [
        migrations.AddField(
            model_name='preferences',
            name='dimensions',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='preferences',
            name='free_methods',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='preferences',
            name='json',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='preferences',
            name='local_pickup',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='preferences',
            name='mode',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
