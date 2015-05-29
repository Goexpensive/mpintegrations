# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MercadoPagoProfile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('mercadopago_user_id', models.BigIntegerField(blank=True)),
                ('access_token', models.CharField(blank=True, max_length=254)),
                ('public_key', models.CharField(blank=True, max_length=254)),
                ('refresh_token', models.CharField(blank=True, max_length=254)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
