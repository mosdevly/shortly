# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-01 18:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20170109_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='custom_id',
            field=models.CharField(blank=True, help_text='Custom short url identifier.', max_length=255, null=True, unique=True),
        ),
    ]