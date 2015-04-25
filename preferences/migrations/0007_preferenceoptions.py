# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preferences', '0006_auto_20150424_0250'),
    ]

    operations = [
        migrations.CreateModel(
            name='PreferenceOptions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('list_fields', models.TextField()),
            ],
        ),
    ]
