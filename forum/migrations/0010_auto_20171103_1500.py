# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-03 15:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0009_auto_20171103_1459'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='thread',
            old_name='user_id',
            new_name='user',
        ),
    ]
