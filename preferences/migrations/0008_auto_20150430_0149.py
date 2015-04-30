# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preferences', '0007_preferenceoptions'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PreferenceOptions',
            new_name='PreferenceTemplates',
        ),
    ]
