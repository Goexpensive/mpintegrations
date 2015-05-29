# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('mercadopago_user_id', models.BigIntegerField(blank=True)),
                ('access_token', models.CharField(max_length=254, blank=True)),
                ('public_key', models.CharField(max_length=254, blank=True)),
                ('refresh_token', models.CharField(max_length=254, blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='mercadopagoprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='MercadoPagoProfile',
        ),
    ]
