# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-05 03:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20171205_0305'),
    ]

    operations = [
        migrations.RenameField(
            model_name='babycrib',
            old_name='date',
            new_name='datetime',
        ),
        migrations.RenameField(
            model_name='breathing',
            old_name='date',
            new_name='datetime',
        ),
        migrations.RenameField(
            model_name='heartbeats',
            old_name='date',
            new_name='datetime',
        ),
        migrations.RenameField(
            model_name='noise',
            old_name='date',
            new_name='datetime',
        ),
        migrations.RenameField(
            model_name='temperature',
            old_name='date',
            new_name='datetime',
        ),
    ]
