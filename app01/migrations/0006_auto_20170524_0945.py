# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-24 01:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0005_host1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='host1',
            name='group',
        ),
        migrations.DeleteModel(
            name='Host1',
        ),
    ]
