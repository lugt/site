# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-24 00:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0055_add_performance_points'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='is_open',
            field=models.BooleanField(default=True, verbose_name='is ticket open?'),
        ),
    ]
