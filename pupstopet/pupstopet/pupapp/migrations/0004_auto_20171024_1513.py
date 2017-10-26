# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-24 19:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pupapp', '0003_auto_20171024_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='endTime',
            field=models.DateTimeField(help_text='time that event ends', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='startTime',
            field=models.DateTimeField(help_text='time that event starts', max_length=10, null=True),
        ),
    ]