# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-30 01:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PupsToPet', '0012_auto_20171029_2133'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['ID', 'start_time', 'end_time', 'location', 'host']},
        ),
        migrations.RenameField(
            model_name='pet',
            old_name='pets_owner',
            new_name='owner',
        ),
        migrations.RemoveField(
            model_name='owner',
            name='owners_pets',
        ),
    ]
