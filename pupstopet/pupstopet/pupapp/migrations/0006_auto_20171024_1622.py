# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-24 20:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pupapp', '0005_auto_20171024_1558'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='owner',
            options={'ordering': ['username', 'id']},
        ),
    ]
