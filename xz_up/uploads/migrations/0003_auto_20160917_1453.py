# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-17 06:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uploads', '0002_auto_20160917_1402'),
    ]

    operations = [
        migrations.RenameField(
            model_name='querykeys',
            old_name='id_number',
            new_name='filepath',
        ),
    ]
