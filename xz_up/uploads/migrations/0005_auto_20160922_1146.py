# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-22 03:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploads', '0004_auto_20160917_1806'),
    ]

    operations = [
        migrations.CreateModel(
            name='queryapply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('busid', models.CharField(max_length=10)),
                ('token', models.CharField(max_length=50)),
                ('usr_name', models.CharField(max_length=12)),
                ('filepath', models.FileField(upload_to='./tmpfiles/tmp')),
                ('usr_datetime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Querykeys',
        ),
    ]
