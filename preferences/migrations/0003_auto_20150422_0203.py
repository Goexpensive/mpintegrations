# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preferences', '0002_auto_20150421_0006'),
    ]

    operations = [
        migrations.RenameField(
            model_name='preferences',
            old_name='items_quantity',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='preferences',
            old_name='items_unit_price',
            new_name='unit_price',
        ),
        migrations.RemoveField(
            model_name='preferences',
            name='items_title',
        ),
        migrations.AddField(
            model_name='preferences',
            name='auto_return',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='preferences',
            name='category_id',
            field=models.CharField(null=True, max_length=254, blank=True),
        ),
        migrations.AddField(
            model_name='preferences',
            name='currency_id',
            field=models.CharField(null=True, max_length=254, blank=True),
        ),
        migrations.AddField(
            model_name='preferences',
            name='default_installments',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='preferences',
            name='default_payment_method_id',
            field=models.CharField(null=True, max_length=254, blank=True),
        ),
        migrations.AddField(
            model_name='preferences',
            name='description',
            field=models.CharField(null=True, max_length=254, blank=True),
        ),
        migrations.AddField(
            model_name='preferences',
            name='email',
            field=models.EmailField(null=True, max_length=254, blank=True),
        ),
        migrations.AddField(
            model_name='preferences',
            name='excluded_payment_methods',
            field=models.CharField(null=True, max_length=254, blank=True),
        ),
        migrations.AddField(
            model_name='preferences',
            name='excluded_payment_types',
            field=models.CharField(null=True, max_length=254, blank=True),
        ),
        migrations.AddField(
            model_name='preferences',
            name='expiration_date_from',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='preferences',
            name='expiration_date_to',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='preferences',
            name='expires',
            field=models.CharField(null=True, max_length=254, blank=True),
        ),
        migrations.AddField(
            model_name='preferences',
            name='failure',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='preferences',
            name='installments',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='preferences',
            name='name',
            field=models.CharField(null=True, max_length=254, blank=True),
        ),
        migrations.AddField(
            model_name='preferences',
            name='pending',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='preferences',
            name='picture_url',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='preferences',
            name='quantity',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='preferences',
            name='success',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='preferences',
            name='surname',
            field=models.CharField(null=True, max_length=254, blank=True),
        ),
        migrations.AlterField(
            model_name='preferences',
            name='external_reference',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='preferences',
            name='init_point',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='preferences',
            name='notification_url',
            field=models.URLField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='preferences',
            name='sandbox_init_point',
            field=models.CharField(max_length=255, blank=True),
        ),
    ]
