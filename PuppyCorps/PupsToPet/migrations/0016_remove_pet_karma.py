# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-30 14:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PupsToPet', '0015_owner_owners_pets'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pet',
            name='karma',
        ),
    ]
