# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Preferences',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('title', models.BigIntegerField()),
                ('quantity', models.CharField(max_length=255)),
                ('unit_price', models.DecimalField(max_digits=10, decimal_places=2)),
                ('notification_url', models.CharField(max_length=255)),
                ('external_reference', models.CharField(max_length=255)),
                ('init_point', models.CharField(max_length=255)),
                ('sandbox_init_point', models.CharField(max_length=255)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('last_modified_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
