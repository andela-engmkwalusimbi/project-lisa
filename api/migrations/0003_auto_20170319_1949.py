# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-19 19:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20170319_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bus',
            name='passenger_seats',
            field=models.IntegerField(max_length=90),
        ),
    ]
